from django import forms
from .models import Article, ArticleCategory, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
