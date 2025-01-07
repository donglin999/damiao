from rest_framework import viewsets
from core.models import Student
from core.api.serializers.student import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    学生视图集
    提供标准的 list、create、retrieve、update、destroy 操作
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 