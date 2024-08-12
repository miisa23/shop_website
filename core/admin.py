from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    list_display_links = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'price', 'author', 'category', 'created_at', 'img_preview']
    list_display_links = ['title']
    list_editable = ['category', 'author']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'created_at', 'text']
    list_display_links = ['product']
    list_editable = ['author', 'text']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Comment, CommentAdmin)
