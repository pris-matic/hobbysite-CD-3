from django.db import models
from django.urls import reverse

# Create your models here.

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Post Categories"

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('forum:getForumThread',args=[self.pk])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createdOn']