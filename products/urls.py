from django.urls import path
from . import views

urlpatterns = [
    path('api/lessons/', views.LessonStatusAPIView.as_view(), name='lessons-api'),
]