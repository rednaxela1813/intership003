from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Lesson, LessonStatus
from .serializers import ProductSerializer, LessonSerializer, LessonStatusSerializer

class AllLessonsListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        products = Product.objects.filter(access=user).prefetch_related('lessons')
        return products

class ProductLessonsListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        product = Product.objects.get(id=product_id, access=user)
        return product.lessons.all()

class ProductStatsView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        product = Product.objects.get(id=product_id, access=user)
        return product
