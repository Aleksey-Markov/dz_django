from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='заголовок')
    slug = models.CharField(max_length=100)
    content = models.TextField(verbose_name='содержимое статьи')
    preview = models.ImageField(upload_to='post/photo', verbose_name='превью', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания')
    is_published = models.BooleanField(verbose_name='признак публикации')
    views_count = models.IntegerField(verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
