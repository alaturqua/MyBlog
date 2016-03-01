from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.

class Entry(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	body = MarkdownField()
	image = models.FileField(null=True, blank=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)
	modified = models.DateTimeField(auto_now_add=False, auto_now=True)

	def get_absolute_url(self):
		return reverse("entry_detail", kwargs={"id": self.id})


	def __str__(self):
	    return self.title

	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]
