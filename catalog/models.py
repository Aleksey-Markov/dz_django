from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование категории')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='название продукта')
    description = models.TextField(verbose_name='описание')
    category_name = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория', null=True, blank=True, related_name='products')
    image = models.ImageField(upload_to='product/photo',verbose_name='превью', null=True, blank=True)
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(verbose_name='дата создания', null=True, blank=True)
    updated_at = models.DateField(verbose_name='дата изменения', null=True, blank=True)

    def __str__(self):
        return f'{self.category_name} {self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
