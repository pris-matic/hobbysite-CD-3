from django.contrib import admin
from .models import Commission, Job, JobApplication

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'description', 'created_on', 'updated_on')
    search_fields = ('title', 'description')
    ordering = ('created_on',)

class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ('commission', 'role', 'manpower_required', 'status')
    search_fields = ('commission', 'role')
    ordering = ['status', '-manpower_required', 'role']

class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication
    list_display = ('job', 'get_applicant_name', 'get_applicant_username', 'status', 'applied_on')
    list_filter = ('status', 'applied_on')
    search_fields = ('job__role', 'applicant__name', 'applicant__user__username')
    ordering = ('status', '-applied_on')

    def get_applicant_name(self, obj):
        return obj.applicant.name
    
    get_applicant_name.short_description = 'Applicant Name'

    def get_applicant_username(self, obj):
        return obj.applicant.user.username
    
    get_applicant_username.short_description = 'Applicant Username'

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
