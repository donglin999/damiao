from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from core.models import Feedback, AnalysisResult
from core.api.serializers.feedback import FeedbackSerializer, AnalysisResultSerializer
from core.services.analysis import analyze_feedback

class FeedbackViewSet(viewsets.ModelViewSet):
    """
    反馈视图集
    提供标准的 list、create、retrieve、update、destroy 操作
    以及自定义的分析操作
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser)

    @action(detail=True, methods=['post'])
    def analyze(self, request, pk=None):
        """
        分析反馈内容
        """
        try:
            feedback = self.get_object()
            print(feedback)
            
            # 调用分析服务
            analysis_result = analyze_feedback(feedback)
            
            if analysis_result:
                serializer = AnalysisResultSerializer(analysis_result)
                return Response(serializer.data)
            return Response(
                {"error": "分析失败"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            ) 