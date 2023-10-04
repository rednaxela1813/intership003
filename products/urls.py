from django.urls import path
from .views import (
    AllLessonsListView,
    ProductLessonsListView,
    ProductStatsView
)

urlpatterns = [
    path('all_lessons/', AllLessonsListView.as_view(), name='all_lessons'),
    path('product_lessons/<int:product_id>/', ProductLessonsListView.as_view(), name='product_lessons'),
    path('product_stats/<int:product_id>/', ProductStatsView.as_view(), name='product_stats'),
]
