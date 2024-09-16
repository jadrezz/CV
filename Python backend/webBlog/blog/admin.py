from django.contrib import admin

from blog.models import Post, Tags, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'author', 'content', 'category', 'tags', 'status')
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', )
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'timestamp_created'

    raw_id_fields = ('author', )
    filter_horizontal = ['tags']


@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    fields = ('tag_name', 'slug')
    list_display = ('tag_name', 'slug')
    prepopulated_fields = {'slug': ('tag_name', )}

admin.site.register(Category)

