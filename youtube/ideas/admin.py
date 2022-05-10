from django.contrib import admin
from .models import Idea, Vote
from django.utils.html import format_html


# Register your models here.

class VoteInLine(admin.TabularInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'show_youtube_url']
    search_fields = ['title']
    list_filter = ['status']
    inlines = [
        VoteInLine
    ]

    def show_youtube_url(self, obj):
        if obj.youtube_url is not None:
            return format_html(f'<a href="{obj.youtube_url}" target="_blank">{"Link"}</a>')
        else:
            return ''

    show_youtube_url.short_description = "URL"


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
