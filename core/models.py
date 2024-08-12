from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара', unique=True)
    short_description = models.TextField(max_length=150, verbose_name='Краткое описание товара')
    full_description = models.TextField(max_length=150, verbose_name='Полное описание товара')
    price = models.TextField(max_length=9, verbose_name='Цена товара', default=0)
    image = models.ImageField(upload_to='articles/', verbose_name='Фото товара')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="100", height="100">')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  related_name='comments', verbose_name='Продукт')
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=10000, verbose_name='Отзыв')

    def __str__(self):
        return f'{self.author}: {self.product}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Like(models.Model):
    user = models.ManyToManyField(User, related_name='likes')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='likes', null=True, blank=True)




