from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    access = models.ManyToManyField(CustomUser, related_name='access')


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    duration = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')


class LessonStatus(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    time_watched = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.time_watched>=(self.lesson.duration*0.8):
            self.status = True
        super(LessonStatus, self).save(*args, **kwargs)


