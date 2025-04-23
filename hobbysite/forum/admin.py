from django.contrib import admin
from .models import ThreadCategory, Thread, Comment

class ThreadInline(admin.TabularInline):
    model = Thread
    extra = 0
    fields = ('title', 'image', 'created_on', 'updated_on',) 
    readonly_fields = ('created_on', 'updated_on',)  

class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory

    list_display = ('name',)
    list_filter = ('name',)
    search_fields =('name',)
    inlines = [ThreadInline]

class ThreadAdmin(admin.ModelAdmin):
    model = Thread

    list_display = ('title', 'author', 'category', 'image', 'created_on', 'updated_on',)
    list_filter = ('category',)
    search_fields =('category__name',)
    readonly_fields = ('created_on', 'updated_on',)

class CommentAdmin(admin.ModelAdmin):
    model = Comment 

    list_display = ('author','thread','created_on','updated_on',)
    list_filter = ('author',)
    search_fields = ('author',)
    readonly_fields = ('created_on', 'updated_on',)  

admin.site.register(ThreadCategory,ThreadCategoryAdmin)
admin.site.register(Thread,ThreadAdmin)
admin.site.register(Comment,CommentAdmin)
