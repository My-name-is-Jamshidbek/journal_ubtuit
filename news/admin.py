from django.contrib import admin
from .models import New

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'creator__username')
    list_filter = ('created_at', 'updated_at', 'creator')
