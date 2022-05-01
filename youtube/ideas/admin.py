from django.contrib import admin
from .models import Idea, Vote


# Register your models here.
@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'youtube_url']
    search_fields = ['title']
    list_filter = ['status']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
