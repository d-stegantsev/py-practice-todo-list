from django.contrib import admin
from .models import Task, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "created_at", "deadline", "is_done")
    list_filter = ("is_done", "created_at", "deadline", "tags")
    search_fields = ("content",)
    filter_horizontal = ("tags",)
    ordering = ("-created_at",)
