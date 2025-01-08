import os
import json
from openai import OpenAI
import httpx
from django.conf import settings
from core.models import Feedback
from core.services.llm_settings import (
    DEEPSEEK_CONFIG,
    SYSTEM_PROMPT,
    ANALYSIS_PROMPT_TEMPLATE,
    HTTP_CLIENT_CONFIG
)

class LLMService:
    def __init__(self):
        # 创建自定义的HTTP客户端
        http_client = httpx.Client(
            base_url=DEEPSEEK_CONFIG["base_url"],
            timeout=HTTP_CLIENT_CONFIG["timeout"],
            follow_redirects=HTTP_CLIENT_CONFIG["follow_redirects"]
        )
        
        # 初始化DeepSeek客户端
        self.client = OpenAI(
            api_key=DEEPSEEK_CONFIG["api_key"],
            base_url=DEEPSEEK_CONFIG["base_url"],
            http_client=http_client
        )
        self.model = DEEPSEEK_CONFIG["model"]

    def get_feedback_history(self, student_id):
        """
        获取学生的所有历史反馈记录
        
        Args:
            student_id: 学生ID
            
        Returns:
            str: 格式化的反馈历史记录
        """
        feedbacks = Feedback.objects.filter(student_id=student_id).order_by('created_at')
        
        if not feedbacks:
            return "暂无历史反馈记录"
        
        history = []
        for feedback in feedbacks:
            history.append(f"时间：{feedback.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                         f"内容：{feedback.content}\n"
                         f"类型：{feedback.feedback_type}\n"
                         f"---")
        
        return "\n".join(history)

    def validate_json_response(self, text):
        """
        验证并清理JSON响应
        
        Args:
            text: API返回的文本
            
        Returns:
            dict: 解析后的JSON对象
        """
        try:
            # 尝试直接解析
            return json.loads(text)
        except json.JSONDecodeError:
            # 如果解析失败，尝试清理文本并重新解析
            try:
                # 查找第一个{和最后一个}之间的内容
                start = text.find('{')
                end = text.rfind('}') + 1
                if start >= 0 and end > start:
                    json_str = text[start:end]
                    return json.loads(json_str)
                raise ValueError("无法找到有效的JSON内容")
            except (json.JSONDecodeError, ValueError) as e:
                raise ValueError(f"JSON验证失败: {str(e)}")

    def analyze_feedback(self, feedback):
        """
        使用DeepSeek大语言模型分析反馈内容
        
        Args:
            feedback: Feedback实例
            
        Returns:
            dict: 包含分析结果的字典
        """
        try:
            # 获取该学生的所有历史反馈
            feedback_history = self.get_feedback_history(feedback.student_id)
            
            # 构建提示词
            prompt = ANALYSIS_PROMPT_TEMPLATE.format(
                feedback_history=feedback_history
            )
            
            # 调用DeepSeek API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt}
                ],
                temperature=DEEPSEEK_CONFIG["temperature"],
                max_tokens=DEEPSEEK_CONFIG["max_tokens"]
            )
            
            # 获取分析结果
            analysis_text = response.choices[0].message.content
            
            # 验证并解析JSON
            analysis = self.validate_json_response(analysis_text)
            
            # 返回结构化数据
            return {
                'raw_analysis': json.dumps(analysis, ensure_ascii=False),
                'summary': analysis.get('summary_for_parents', '通过DeepSeek大语言模型分析完成'),
                'feedback_history': feedback_history
            }
            
        except Exception as e:
            print(f"LLM分析失败: {str(e)}")
            return None 