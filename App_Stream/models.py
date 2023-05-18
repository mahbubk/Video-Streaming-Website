from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    group = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group

    class Meta:
        verbose_name_plural = 'Categories'


class Video(models.Model):
    title = models.CharField(max_length=264)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'category')
    link = models.URLField(blank=True)
    detail_text = models.TextField(max_length=1000, verbose_name='Description')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created',]


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='user_vedio')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment  = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment
