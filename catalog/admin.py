from django.contrib import admin

from catalog.models import Product, Category, Version
from blog.models import Post


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'title', 'price',)
    list_filter = ('category_name',)
    search_fields = ('title', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_published',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_name', 'num_of_version', 'is_active_version',)
    list_filter = ('is_active_version',)
