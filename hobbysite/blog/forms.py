from django import forms
from .models import Comment, Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
        widgets = {
            'entry': forms.Textarea(attrs={
                'rows': 1,
                'placeholder': 'Write your comment here...',
                'class': 'form-control'
            })
        }

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry', 'header_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'entry': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Write your article here...',
                'class': 'form-control'
            }),
            'header_image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }
