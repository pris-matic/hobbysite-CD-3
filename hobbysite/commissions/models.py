from django.db import models

class Commission(models.Model):
    STATUS_STATES = [
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discountinued', 'Discountinued'),
    ]

    title = models.CharField(max_length=255)    
    description = models.TextField()
    people_required = models.PositiveIntegerField()
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

