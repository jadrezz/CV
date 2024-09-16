# Generated by Django 5.0.6 on 2024-09-08 07:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'blog_categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=255)),
                ('comment_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-comment_created'],
            },
        ),
        migrations.CreateModel(
            name='LeftMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('need_answer', models.BooleanField(default=False)),
                ('content', models.TextField()),
                ('answered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField(blank=True, verbose_name='Содержимое')),
                ('status', models.CharField(choices=[('DF', 'Черновик'), ('PB', 'Опубликовано')], default='DF', max_length=2, verbose_name='Статус')),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_edited', models.DateTimeField(auto_now=True)),
                ('total_seen', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'blog_posts',
                'ordering': ['-timestamp_created'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=256, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'blog_tags',
            },
        ),
    ]
