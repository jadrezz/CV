from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import F
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from blog.forms import LeaveMessageForm, LeaveComment, AddArticle
from blog.models import Post, Category, Tags, LeftMessage, Comment
from blog.utils import RussianSlugify


def index(request):
    posts = Post.published.all().select_related('author')
    paginator = Paginator(posts, 3)
    page_obj = paginator.get_page(request.GET.get('page', 1))
    context = {
        'title': 'Главная страница',
        'posts': page_obj,
        'selected_id': 1,
        'paginator': paginator,
    }
    return render(request, 'blog/index.html', context)


def categories(request):
    context = {
        'title': 'Категории',
        'selected_id': 2,
    }
    return render(request, 'blog/categories.html', context)


def read_article(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    if not request.session.get(f'viewed_{post_slug}', False):
        Post.objects.filter(pk=post.pk).update(total_seen=F('total_seen') + 1)
        request.session[f'viewed_{post_slug}'] = True
    if request.method == 'POST':
        form = LeaveComment(request.POST)
        if form.is_valid():
            try:
                if request.session.get(f'commented_{post_slug}', False) \
                        and not request.user.is_authenticated: # проверка на повторное добавление
                    raise Exception()
                author = None if not request.user.username else request.user
                Comment.objects.create(post=post, comment=form.cleaned_data['comment'], author=author)
                messages.success(request, 'Комментарий успешно добавлен!', extra_tags='CommentLeft')
                request.session[f'commented_{post_slug}'] = True
                form = LeaveComment()
            except:
                form.add_error(None, 'Произошла ошибка добавления комментария')
    else:
        form = LeaveComment()

    context = {
        'title': post.title,
        'post': post,
        'form': form,
        'comment_left': request.session.get(f'commented_{post_slug}', False)
    }
    return render(request, 'blog/read_article.html', context)


def show_cat_posts(request, category_slug):
    cat = get_object_or_404(Category, slug=category_slug)
    posts = Post.published.filter(category=cat).select_related('author')
    context = {
        'title': cat.cat_name,
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def show_tag_posts(request, tag_slug):
    tag = Tags.objects.get(slug=tag_slug)
    posts = Post.published.filter(tags=tag).select_related('author')
    context = {
        'title': tag.tag_name.title(),
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return index(request)


def contacts(request):
    if request.method == 'POST':
        form = LeaveMessageForm(request.POST)
        if form.is_valid():
            try:
                LeftMessage.objects.create(**form.cleaned_data)
                messages.success(request, 'Ваше сообщение успешно отправлено!')
            except:
                form.add_error(None, 'Произошла ошибка отправки')
    else:
        form = LeaveMessageForm()

    context = {
        'title': 'Оставить сообщение',
        'form': form,
        'selected_id': 4
    }
    return render(request, 'blog/contacts.html', context)


@login_required(login_url='users:login')
def add_article(request):
    if request.method == 'POST':
        form = AddArticle(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(RussianSlugify.slugify(post.title))
            post.save()
            messages.success(request, "Статья успешно добавлена!", extra_tags="Added")
            return redirect('read_article', post_slug=post.slug)
    else:
        form = AddArticle()

    return render(request, 'blog/add_article.html', {'form': form})