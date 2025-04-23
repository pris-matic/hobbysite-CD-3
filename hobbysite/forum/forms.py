from django import forms
from .models import ThreadCategory, Thread, Comment

class ThreadCategoryForm(forms.modelForm):
    class Meta:
        model = ThreadCategory
        fields = ['name','description']

class ThreadForm(forms.modelForm):
    class Meta:
        model = Thread
        fields = ['title','category','entry','image']

class CommentForm(forms.modelForm):
    class Meta:
        model = Comment
        fields = ['entry']