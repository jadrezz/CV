from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/', views.categories, name='show_all_cats'),
    path('categories/<slug:category_slug>/', views.show_cat_posts, name='show_cat_posts'),
    path('article/<slug:post_slug>', views.read_article, name='read_article'),
    path('tags/<slug:tag_slug>', views.show_tag_posts, name='show_tag_posts'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('add-article/', views.add_article, name='add_article'),

]
