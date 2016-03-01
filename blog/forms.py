from django import forms
from .models import Entry



class BlogEntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = [
			'author',
			'title',
			'body',
			'image',
		]