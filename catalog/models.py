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
    image = models.ImageField(upload_to='product/photo', verbose_name='фото', null=True, blank=True)
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(verbose_name='дата создания', null=True, blank=True)
    updated_at = models.DateField(verbose_name='дата изменения', null=True, blank=True)

    def __str__(self):
        return (f'Категория: {self.category_name}, наименование: {self.title}, цена: {self.price}руб., описание: {self.description}.')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, verbose_name='продукт', related_name='versions')
    num_of_version = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=150, verbose_name='название версии')
    is_active_version = models.BooleanField(default=True, verbose_name='теущая версия')

    def __str__(self):
        return f'{self.version_name} - {self.num_of_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

