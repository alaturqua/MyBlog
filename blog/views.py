from django.views import generic
from . import models
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Entry
from django.utils import timezone
from .forms import BlogEntryForm

# Create your views here.


class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 10

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

def BlogCreate(request):
	form = BlogEntryForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		'form':form,
	}
	return render(request,"post_edit.html", context)


