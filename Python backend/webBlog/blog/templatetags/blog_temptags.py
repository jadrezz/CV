from django import template
from django.db.models import Count

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/temptags/show_categories.html')
def show_categories():
    categories = Category.objects.annotate(total=Count('posts')).filter(total__gte=1)
    return {'categories': categories}


@register.inclusion_tag('blog/temptags/show_comments.html')
def show_comments(post):
    comments = post.comments.all()
    return {'comments': comments}
