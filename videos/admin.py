from django.contrib import admin
from .models import Videos, YoutubeKeys

# Register your models here.

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_at')
    list_display_links = ('id', 'title', )
    date_hierarchy = 'published_at'
    show_full_result_count = False



@admin.register(YoutubeKeys)
class YoutubeKeysAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'added_at')
    list_display_links = ('id', 'key', )
    date_hierarchy = 'added_at'
    show_full_result_count = False