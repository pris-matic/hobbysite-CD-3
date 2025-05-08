from django.contrib import admin
from .models import ArticleCategory, Article, Comment

# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    list_display = ('name', 'description',)
    search_fields = ('name',)
    list_filter = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'category', 'created_on', 'updated_on')
    search_fields = ('title',)
    list_filter = ('category', 'created_on', 'updated_on')

class CommentAdmin(admin.ModelAdmin):
    model = Comment

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
