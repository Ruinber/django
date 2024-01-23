# Generated by Django 4.2.7 on 2023-11-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('message', models.TextField(max_length=3000, verbose_name='Описание проекта')),
                ('photo', models.ImageField(blank=True, default=None, upload_to='', verbose_name='Фото')),
            ],
        ),
    ]
