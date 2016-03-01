from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
	title = 'Newsletter'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	
	if form.is_valid():
		form.save()
		# instance = form.save(commit=False)
		# full_name = ""
		# if not full_name:
		# 	full_name = "Mr. Email Receiver"
		# instance.full_name = full_name
		# # if not instance.full_name:
		# # 	instance.full_name = "Mr. Email Receiver"
		# instance.save()
		context = {
			"title": "Thank You!",
		}
	
	return render(request, "newsletter.html", context)



def contact(request):
	title = "Contact Us"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#for key, value in form.cleaned_data:
		contact_email = form.cleaned_data.get("contact_email")
		contact_message = form.cleaned_data.get("contact_message")
		form_full_name = form.cleaned_data.get("form_full_name")
		subject = "Site contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [form_full_name, 'yourothermail@hotmail.de']
		message = "%s: %s via %s"%(
			form_full_name, 
			contact_message, 
			contact_email)
		send_mail(
			subject, 
			message, 
			from_email, 
			[to_email], 
			fail_silently=True)

	context = {
		"form": form,
		"title": title,

	}

	return render(request, "forms.html", context)