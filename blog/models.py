from django.db import models
from django.contrib.auth.models import User
import os
# from turtle import mode
# from django.db import models

# Create your models here.

Class Tag


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # NOTE: 한글 입력 allow_unicode ture
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.pk}'

    class Meta:
        verbose_name_plural: 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', null=True, blank=True)
    attached_file = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # NOTE: nullable
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    #methods
    def __str__(self):
        return f'[{self.pk}]  [{self.title}]'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.attached_file.name)
