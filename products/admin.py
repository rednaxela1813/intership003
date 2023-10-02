from django.contrib import admin
from .models import Product, Lesson, LessonStatus


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'owner')


admin.site.register(Product, ProductAdmin)


