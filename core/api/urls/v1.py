from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api.views.student import StudentViewSet
from core.api.views.feedback import FeedbackViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 