from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    """学生模型"""
    name = models.CharField('姓名', max_length=100)
    student_id = models.CharField('学号', max_length=20, unique=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.student_id})"

class Feedback(models.Model):
    """反馈模型"""
    FEEDBACK_TYPE_CHOICES = (
        ('text', '文字'),
        ('audio', '音频'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='feedbacks', verbose_name='学生')
    feedback_type = models.CharField('反馈类型', max_length=10, choices=FEEDBACK_TYPE_CHOICES)
    content = models.TextField('反馈内容')
    audio_file = models.FileField('音频文件', upload_to='audio_feedback/', null=True, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '反馈'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.name}的{self.get_feedback_type_display()}反馈"

class AnalysisResult(models.Model):
    """分析结果模型"""
    feedback = models.OneToOneField(Feedback, on_delete=models.CASCADE, related_name='analysis', verbose_name='反馈')
    structured_data = models.JSONField('结构化数据')
    summary = models.TextField('总结')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '分析结果'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.feedback.student.name}的反馈分析"
