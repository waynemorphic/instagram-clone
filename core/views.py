from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms import UserLoginForm, UserRegistrationForm

# Create your views here.

# index function to render index template file
def index(request):
    return render(request, 'home/index.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            full_name = form.cleaned_data['full_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return HttpResponseRedirect('Registration Successful')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'django_registration/registration.html', {"form": form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm()
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return HttpResponseRedirect(f'{{current_user}} Login Successful')
    else:
        form = UserLoginForm()
    
    return render(request, 'django_registration/login.html', {"form": form})
        