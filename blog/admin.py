from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
# Register your models here.


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "author", "publish", "modified", "created",)

admin.site.register(models.Entry, EntryAdmin)