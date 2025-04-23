from django.db import models
from django.urls import reverse

class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Thread Categories"

class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = 'placeholder'
    category = models.ForeignKey(ThreadCategory, on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('forum:get_forum_thread',args=[self.pk])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']

class Comment(models.Model):
    author = 'placeholder'
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.thread

    class Meta:
        ordering = ['created_on']