from django.contrib import admin
from .models import Product, Lesson, LessonStatus


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'owner')


class LessonStatusAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'user', 'status')


admin.site.register(Product, ProductAdmin)

admin.site.register(LessonStatus, LessonStatusAdmin)


