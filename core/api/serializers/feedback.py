from rest_framework import serializers
from core.models import Feedback, AnalysisResult

class AnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisResult
        fields = ['id', 'structured_data', 'summary', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class FeedbackSerializer(serializers.ModelSerializer):
    analysis = AnalysisResultSerializer(read_only=True)
    
    class Meta:
        model = Feedback
        fields = ['id', 'student', 'feedback_type', 'content', 'audio_file', 'analysis', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at'] 