from django.contrib import admin
from .models import Article, ArticleCategory

# Register your models here.

class ArticleInline(admin.TabularInline):
    model = Article
    fields = ['title','category']

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    search_fields = ('name',)
    list_display = ('name', 'description')
    inlines = [
            ArticleInline,
            ]

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ('title', 'category', 'entry')
    list_filter = ('category',)
    list_display = ('title', 'category', 'created_on', 'updated_on')

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
