import uuid

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse

from users.models import MyUser


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class PendingMessage(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(answered=False)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Черновик'
        PUBLISHED = 'PB', 'Опубликовано'

    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200, null=False, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, null=False)
    content = models.TextField(blank=True, verbose_name='Содержимое')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, related_name='posts')
    tags = models.ManyToManyField('Tags', related_name='posts', blank=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT,
                              verbose_name='Статус')
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_edited = models.DateTimeField(auto_now=True)
    total_seen = models.IntegerField(default=0)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('read_article', kwargs={'post_slug': self.slug})

    class Meta:
        db_table = 'blog_posts'
        ordering = ['-timestamp_created']
        indexes = [
            models.Index(fields=['-timestamp_created', 'slug']),
        ]


class Category(models.Model):
    cat_name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, null=False, db_index=True)

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('show_cat_posts', kwargs={'category_slug': self.slug})

    class Meta:
        db_table = 'blog_categories'


class Tags(models.Model):
    tag_name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(unique=True, null=False, db_index=True)

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse('show_tag_posts', kwargs={'tag_slug': self.slug})

    class Meta:
        db_table = 'blog_tags'


class LeftMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    need_answer = models.BooleanField(default=False)
    content = models.TextField(null=False)
    answered = models.BooleanField(default=False)
    objects = models.Manager()
    pending = PendingMessage()

    def __str__(self):
        return self.name, self.email


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=255, null=False)
    comment_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-comment_created']
        indexes = [
            models.Index(fields=['id', '-comment_created'])
        ]

