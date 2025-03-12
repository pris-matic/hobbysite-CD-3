from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    createdOn = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
    
    class Meta:
        ordering = ['-createdOn']
    
    def save(self, *args, **kwargs):
        self.post.updatedOn = now()
        self.post.save(update_fields=['updatedOn'])
        super().save(*args, **kwargs)
