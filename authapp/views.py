from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userRegisterForm

# Create your views here.
def register(request):
	#form that pass into template
	#classes -> db; classes ->form
	if request.method == "POST":
		form = userRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"Account created for {username}")
			return redirect("login")
	else:
		form = userRegisterForm()


	
	return render(request, 'authapp/register.html', {'form': form})


def profile(request):
	return render(request, 'authapp/profile.html')