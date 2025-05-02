from django.contrib import admin
from .models import Article, ArticleCategory

# Register your models here.

class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    search_fields = ('name',)
    list_display = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    fields = [('title','category'),'header_image','author','entry']
    search_fields = ('title', 'category', 'author', 'entry')
    list_filter = ('category', 'author')
    list_display = ('title', 'category', 'author', 'created_on', 'updated_on')


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
