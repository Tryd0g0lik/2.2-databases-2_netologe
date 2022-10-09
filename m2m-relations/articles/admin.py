from django.contrib import admin

from .models import Article, Category, ArticleCategory


class ArticleCategoryInline(admin.TabularInline):

    model = ArticleCategory
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'checkbox']
    list_filter = ['published_at', 'categories']
    inlines = [ArticleCategoryInline, ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']

