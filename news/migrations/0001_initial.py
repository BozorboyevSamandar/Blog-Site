# Generated by Django 3.2.5 on 2021-07-15 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Bo`lim nomi')),
            ],
            options={
                'verbose_name': 'Bo`lim',
                'verbose_name_plural': 'Bo`lim',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Sarlavha')),
                ('content', models.TextField(blank=True, verbose_name='Tarif')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Qo`shilgan vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqt')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Rasm')),
                ('is_published', models.BooleanField(default=True, verbose_name='Nashir qilindi')),
                ('category', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category')),
            ],
            options={
                'verbose_name': 'Xabarlar',
                'verbose_name_plural': 'Xabarlar',
                'ordering': ['-created_at'],
            },
        ),
    ]