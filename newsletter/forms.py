from django import forms
from .models import SignUp


class ContactForm(forms.Form):
	form_full_name = forms.CharField(required=False)
	contact_email = forms.EmailField()
	contact_message= forms.CharField()

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']



	# def clean_full_name(self):
	# 	full_name = self.cleaned.data.get('full_name')
	# 	return full_name

