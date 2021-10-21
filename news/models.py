from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Sarlavha')
    content = models.TextField(blank=True, verbose_name='Tarif')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Qo`shilgan vaqt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqt')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Rasm', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Nashir qilindi')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, default=1, verbose_name='Bo`lim')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xabarlar'
        verbose_name_plural = 'Xabarlar'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Bo`lim nomi')

    class Meta:
        verbose_name = 'Bo`lim'
        verbose_name_plural = 'Bo`lim'
        ordering = ['title']

    def __str__(self):
        return self.title
