from django.db import models

from user_management.models import Profile

class Commission(models.Model):
    STATUS_STATES = [
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discountinued', 'Discountinued'),
    ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)    
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_STATES, default='Open')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']

class Job(models.Model):
    STATUS_STATES = [
        ('Open', 'Open'),
        ('Full', 'Full'),
    ]

    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='jobs')
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_STATES, default='Open')

    def __str__(self):
        return f"{self.role} ({self.status})"

    class Meta:
        ordering = ['status', '-manpower_required', 'role']
    
class JobApplication(models.Model):
    STATUS_STATES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_STATES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return f"{self.applicant.name} - {self.status}"

    class Meta:
        ordering = [
            models.Case(
                models.When(status='Pending', then=1),
                models.When(status='Accepted', then=2),
                models.When(status='Rejected', then=3),
                output_field=models.IntegerField()
                ),
            '-applied_on'
        ]
