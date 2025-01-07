from rest_framework import serializers
from core.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'student_id', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at'] 