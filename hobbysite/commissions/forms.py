from django import forms
from django.forms import inlineformset_factory
from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        exclude = ['author','created_on','updated_on']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter commission title'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Enter commission description...',
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role','manpower_required','status']
        widgets = {
            'role': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job role'
            }),
            'manpower_required': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Required number of people'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

JobFormSet = inlineformset_factory(
    Commission,
    Job,
    form=JobForm,
    fields=('role', 'manpower_required', 'status'),
    extra=1,
    can_delete=False
)

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ['applicant', 'applied_on']
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }