from django.contrib import admin
from .models import Videos

# Register your models here.

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_at')
    list_display_links = ('id', 'title', )
    date_hierarchy = 'published_at'
    show_full_result_count = False