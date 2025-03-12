from django.db import models
from django.urls import reverse

# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = "Article category"
        verbose_name_plural = "Article categories"
        ordering = ['name']
        unique_together = ['name']

class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL, related_name='article')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = [['title','created_on']]

