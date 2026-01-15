from django.db import models
from django.core.exceptions import ValidationError


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    published_at = models.DateTimeField(verbose_name="Дата публикации")
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение")
    
    # Связь многие-ко-многим через промежуточную модель Scope
    tags = models.ManyToManyField(
        Tag,
        through='Scope',
        related_name='articles',
        verbose_name="Разделы"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-published_at']


class Scope(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='scopes',
        verbose_name="Статья"
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='scopes',
        verbose_name="Раздел"
    )
    is_main = models.BooleanField(default=False, verbose_name="Основной")

    class Meta:
        verbose_name = "Связь статья-раздел"
        verbose_name_plural = "Связи статья-раздел"
        # Гарантируем уникальность связки статья-раздел
        unique_together = [['article', 'tag']]
        ordering = ['-is_main', 'tag__name']
