from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from embed_video.admin import AdminVideoMixin

# Register your models here.


class EntryAdmin(AdminVideoMixin, MarkdownModelAdmin):
    list_display = ("title", "author", "publish", "modified", "created",)

admin.site.register(models.Entry, EntryAdmin)