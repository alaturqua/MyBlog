from django.contrib import admin
from .models import SignUp
from .forms import SignUpForm

# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__str__","full_name", "timestamp", "updated"]
	form = SignUpForm

admin.site.register(SignUp, SignUpAdmin)