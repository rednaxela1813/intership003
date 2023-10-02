from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import LessonStatus
from .serializers import LessonStatusSerializer


class LessonStatusAPIView(generics.ListAPIView):
    serializer_class = LessonStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return LessonStatus.objects.filter(user=user)

