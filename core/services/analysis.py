from core.models import AnalysisResult
from core.services.llm import LLMService

def analyze_feedback(feedback):
    """
    分析反馈内容
    
    Args:
        feedback: Feedback实例
    
    Returns:
        AnalysisResult实例
    """
    try:
        # 创建LLM服务实例
        llm_service = LLMService()
        
        # 使用LLM分析反馈内容
        analysis_result = llm_service.analyze_feedback(feedback)
        
        if not analysis_result:
            raise Exception("LLM分析失败")
        
        # 创建或更新分析结果
        result, created = AnalysisResult.objects.update_or_create(
            feedback=feedback,
            defaults={
                'structured_data': analysis_result['raw_analysis'],
                'summary': analysis_result['summary'],
                'feedback_history': analysis_result['feedback_history']
            }
        )
        
        return result
    except Exception as e:
        print(f"分析失败: {str(e)}")
        return None 