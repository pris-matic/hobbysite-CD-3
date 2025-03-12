from django.contrib import admin
from .models import Article, ArticleCategory

# Register your models here.

class ArticleInline(admin.StackedInline):
    model = Article
    fields = ['title','category','entry']

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    search_fields = ("title",)
    inlines = [
            ArticleInline,
            ]

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ("title", "category", "entry")
    list_filter = ("title","category",)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
