from django.db import models

# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    content = models.TextField(null=True, blank=True, verbose_name="Содержание")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")

    rubric = models.ForeignKey('Categories', null=True, on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Обьявления"
        verbose_name = "Обьявление"
        ordering = ['-published']

class Categories(models.Model):
    name = models.CharField(max_length=20, verbose_name="Категория : ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ['-name']
