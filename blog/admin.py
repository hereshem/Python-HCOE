from django.contrib import admin

# Register your models here.

from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'created', 'modified')
    list_filter = ['created', 'title']
    search_fields = ['title', 'description', 'author']

admin.site.register(Blog, BlogAdmin)