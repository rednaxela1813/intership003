from rest_framework import serializers
from .models import Product, Lesson, LessonStatus


class LessonStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonStatus
        fields = ['lesson', 'user', 'status', 'time_watched']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['name', 'link', 'duration', 'product']


class ProductSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    access = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = ['name', 'owner', 'access', 'lessons']

    def create(self, validated_data):
        user = self.context['request'].user
        product = Product.objects.create(owner=user, **validated_data)
        return product