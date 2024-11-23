from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'gender', 'is_superuser')
    list_filter = ('gender', 'status',)
    search_fields = ('username', 'email')
    list_per_page = 10

# Register your models here.
admin.site.register(User, UserAdmin)