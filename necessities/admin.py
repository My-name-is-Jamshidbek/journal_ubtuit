from django.contrib import admin
from .models import Necessities


@admin.register(Necessities)
class NecessitiesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']  # Add other fields if needed
