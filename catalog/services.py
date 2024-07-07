from django.core.cache import cache

from django.conf import settings

from catalog.models import Category


def get_categories(product_pk):
    if settings.CACHE_ENABLED:
        key = f'category_list_{product_pk}'
        category_list = cache.get(key)
        if not category_list:
            category_list = Category.objects.filter(pk=product_pk)
            cache.set(key, category_list)
    else:
        category_list = Category.objects.filter(pk=product_pk)

    return category_list
