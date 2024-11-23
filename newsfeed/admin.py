from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'image',)
    list_filter = ('user__username',)
    search_fields = ('user__username', 'body')
    list_per_page = 10

# Register your models here.
admin.site.register(Post, PostAdmin)