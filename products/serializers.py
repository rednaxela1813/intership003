from rest_framework import serializers
from .models import Product, Lesson, LessonStatus

class LessonStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonStatus
        fields = ['status', 'time_watched']

class LessonSerializer(serializers.ModelSerializer):
    lesson_status = LessonStatusSerializer(many=True, read_only=True, source='lessonstatus_set')

    class Meta:
        model = Lesson
        fields = ['name', 'link', 'duration', 'lesson_status']

class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField()
    access = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['name', 'owner', 'access', 'lessons']
