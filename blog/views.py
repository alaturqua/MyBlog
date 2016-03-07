from . import models
from django.shortcuts import render, get_object_or_404
from .forms import BlogEntryForm
from django.http import HttpResponseRedirect

# Create your views here.


def BlogIndex(request):
	queryset = models.Entry.objects.all()
	context = {
		"object_list": queryset,
		"title": "list"
	}
	return render(request, "home.html", context)


def BlogDetail(request, id):
	instance = get_object_or_404(models.Entry, id=id)
	context = {
		"title": instance.title,

		"instance":instance,
	}
	return render(request, "post.html", context)


def BlogCreate(request):
	form = BlogEntryForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		'form':form,
	}
	return render(request,"post_edit.html", context)


def BlogUpdate(request, id=None):
	instance = get_object_or_404(models.Entry, id=id)
	form = BlogEntryForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"author": instance.author,
		"title": instance.title,
		"body": instance.body,
		"image": instance.image,
		"form": form,
	}

	return render(request, "post_edit.html", context)


