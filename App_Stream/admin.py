from django.contrib import admin
from App_Stream.models import Category, Video, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Comment)
