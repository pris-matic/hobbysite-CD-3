from django.contrib import admin
from .models import Commission, Comment

# Register your models here.

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = ('title', 'description', 'people_required', 'created_on', 'updated_on')
    search_fields = ('title', 'description')
    ordering = ('created_on',)

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('commission', 'entry', 'created_on', 'updated_on')
    search_fields = ('commission', 'entry')
    ordering = ('-created_on',)

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)
