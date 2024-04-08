# accounts/admin.py

from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']  # Add filter options for status and created_at fields

admin.site.register(Article, ArticleAdmin)
