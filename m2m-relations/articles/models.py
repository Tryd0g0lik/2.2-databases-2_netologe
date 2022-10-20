from django.db import models
from django.contrib import admin



class Article(models.Model):

    title = models.CharField(max_length=256,
                             verbose_name='Название')
    text = models.TextField(verbose_name='Текст')

    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True,
                              verbose_name='Изображение')

    # category = models.ManyToManyField(
    #   'Category',
    #   through='ArticleCategory',
    #   related_name='articles'
    # )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Category(models.Model):
    category = models.CharField(max_length=30,
                                db_index=True,
                                verbose_name='Категория')
    articles = models.ManyToManyField(
      'Article',
      related_name='category',
      through='ArticleCategory',

    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category

class ArticleCategory(models.Model):
    articles = models.ForeignKey(Article, on_delete=models.CASCADE,
                                 related_name='scopes',
                                 verbose_name='Категории')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE,
                                   related_name='scopes',
                                   verbose_name='Категории')
    checkbox_main = models.BooleanField(default=False,
                                        verbose_name='Основной')

