from django.contrib import admin
from .models import Commission, Job

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'description', 'people_required', 'created_on', 'updated_on')
    search_fields = ('title', 'description')
    ordering = ('created_on',)

class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ('commission', 'role', 'manpower_required', 'status')
    search_fields = ('commission', 'role')
    ordering = ['status', '-manpower_required', 'role']

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
