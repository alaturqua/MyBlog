from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse
from django.utils import timezone
from autoslug import AutoSlugField

# Create your models here.

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	body = MarkdownField()
	image = models.FileField(null=True, blank=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	slug = AutoSlugField(populate_from="title", unique_with='publish')

	objects = EntryQuerySet.as_manager()

	def get_absolute_url(self):
		return reverse("entry_detail", kwargs={"slug": self.slug})


	def __str__(self):
	    return self.title

	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]
