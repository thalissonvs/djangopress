from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'pub_date', 'status']
    list_filter = ['status', 'created_at', 'pub_date', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'pub_date'
    ordering = ['status', 'pub_date']
    show_facets = admin.ShowFacets.ALWAYS


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created_at', 'active']
    list_filter = ['created_at', 'updated_at', 'active']
    search_fields = ['name', 'email', 'body']