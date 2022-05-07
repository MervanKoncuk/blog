from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date')
    list_display_links = ('id',)
    list_filter = ('created_date',)
# Register your models here.
admin.site.register(Post, PostAdmin)