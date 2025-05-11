from django.contrib import admin
from .models import ArticleCategory, Article, Comment

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    list_display = ('name', 'description',)
    search_fields = ('name',)
    list_filter = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    list_display = ('title', 'author', 'category', 'created_on', 'updated_on', 'header_image')
    search_fields = ('title',)
    list_filter = ('author', 'category', 'created_on', 'updated_on')

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('article', 'entry', 'author', 'created_on')
    search_fields = ('entry',)
    list_filter = ('article', 'author', 'created_on')

admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
