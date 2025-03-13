from django.contrib import admin
from .models import PostCategory, Post

# Register your models here.

class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    fields = ('title', 'created_on', 'updated_on') 
    readonly_fields = ('created_on', 'updated_on')  

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory

    list_display = ('name',)
    list_filter = ('name',)
    search_fields =('name',)
    inlines = [PostInline]

class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = ('title', 'category', 'created_on', 'updated_on',)
    list_filter = ('category',)
    search_fields =('category__name',)
    readonly_fields = ('created_on', 'updated_on') 

admin.site.register(PostCategory,PostCategoryAdmin)
admin.site.register(Post,PostAdmin)
