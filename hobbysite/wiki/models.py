from django.db import models
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = "Article category"
        verbose_name_plural = "Article categories"
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='articles')
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL, related_name='articles')
    entry = models.TextField()
    header_image = models.ImageField(upload_to="wiki/")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment on {self.article.title} by {self.author} on {self.created_on}:\n{self.entry}"
