from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'firstname', 'lastname', 'institution', 'city', 'country', 'academic_degree')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'firstname', 'lastname', 'institution', 'city', 'country', 'academic_degree')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'firstname', 'lastname', 'institution', 'city', 'country', 'academic_degree')}
        ),
    )
    search_fields = ('username', 'email', 'firstname', 'lastname', 'institution', 'city', 'country', 'academic_degree')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
