from django.db import models
from django.urls import reverse

# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        unique_together = ['name']

class Article(models.Model):
    title = models.CharField(max_length=255)
    entry = models.TextField()
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, related_name='article')
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = [['title','created_on']]

