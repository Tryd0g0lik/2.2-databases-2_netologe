from django.contrib import admin

from .models import Article, Category, CategoryArticle


class CategoryInline(admin.TabularInline):
    model = CategoryArticle
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    list_filter = ['published_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    inlines = [CategoryInline,]
