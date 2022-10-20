from django.contrib import admin

from .models import Article, Category, ArticleCategory


class ArticleAdminInline(admin.TabularInline):

    model = ArticleCategory
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    list_filter = ['published_at']

    inlines = [ArticleAdminInline, ]
    # pubs = Article.objects.select_related('id', 'title', 'text',
    #                                       'published_at',
    #                                       'category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category',]


