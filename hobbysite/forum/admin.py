from django.contrib import admin
from django.contrib.auth.models import User
from .models import PostCategory, Post, Profile, Comment

# Register your models here.

class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    fields = ('title', 'createdOn', 'updatedOn') 
    readonly_fields = ('createdOn', 'updatedOn')  

class PostCategoryAdmin(admin.ModelAdmin):
    model = PostCategory

    list_display = ('name',)
    list_filter = ('name',)
    search_fields =('name',)
    inlines = [PostInline]

class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = ('title', 'category', 'createdOn', 'updatedOn',)
    list_filter = ('category',)
    search_fields =('category__name',)
    readonly_fields = ('createdOn', 'updatedOn') 

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False

class UserAdmin(admin.ModelAdmin):
	inlines = [ProfileInline]
      
class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ('author', 'post', 'createdOn',)
    list_filter = ('author', 'post',)
    readonly_fields = ('createdOn',)

admin.site.register(PostCategory,PostCategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)