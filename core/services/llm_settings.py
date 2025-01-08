# DeepSeek API配置
DEEPSEEK_CONFIG = {
    "api_key": "sk-e67221ed8f3c449b8bb994d564f124ed",
    "base_url": "https://api.deepseek.com/v1",
    "model": "deepseek-chat",
    "temperature": 0.7,
    "max_tokens": 1000
}

# 系统提示词
SYSTEM_PROMPT = """你是一个专业的教育反馈分析专家。
你的任务是分析学生的历史反馈记录，理解学生的学习状况、行为表现和情感变化。
请特别注意反馈的时间顺序，识别学生在不同时期的变化趋势。
生成的是一个整体汇报给到家长，需要言辞温柔，不能出现明显的负面评价，例如打架、暴力等等，尽可能的给出正面的评价。
你需要以JSON格式返回分析结果，确保JSON格式完整且有效。
"""

# 分析提示词模板
ANALYSIS_PROMPT_TEMPLATE = """
请分析以下学生的所有历史反馈记录，并提供全面的分析结果。

学生反馈历史：
{feedback_history}

请从以下几个方面进行分析，并将分析结果以严格的JSON格式返回。
注意：
1. 必须返回完整的JSON对象
2. 所有字符串需要使用双引号
3. 不要包含任何JSON之外的内容
4. 确保JSON格式的正确性和完整性

返回格式示例：
{{
    "sentiment_trend": "描述情感倾向的变化趋势",
    "main_issues": [
        "主要问题1",
        "主要问题2"
    ],
    "behavior_analysis": "描述学习态度和行为表现",
    "time_based_changes": "描述时间维度的变化趋势",
    "recommendations": [
        "建议1",
        "建议2"
    ],
    "summary_for_parents": "面向家长的总结性描述"
}}

请确保返回的JSON严格遵循上述格式。"""

# HTTP客户端配置
HTTP_CLIENT_CONFIG = {
    "timeout": 60.0,
    "follow_redirects": True
} 