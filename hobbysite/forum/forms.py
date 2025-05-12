from django import forms
from .models import ThreadCategory, Thread, Comment

class ThreadCategoryForm(forms.ModelForm):
    class Meta:
        model = ThreadCategory
        fields = ['name','description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Write your article here...',
                'class': 'form-control'
            }),
        }

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title','category','entry','image']
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