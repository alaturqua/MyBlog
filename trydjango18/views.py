from django.shortcuts import render


# Create your views here.

def about(request):
	""" Building the about Page """
	return render(request, "about.html", {})