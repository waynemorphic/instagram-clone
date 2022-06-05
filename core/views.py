from email.mime import image
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from core.forms import UserLoginForm, UserRegistrationForm, CommentForm, NewPostForm, ProfileForm
from core.models import User_Model, Profile_Model, Image_Model

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
            return redirect('home')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'django_registration/registration.html', {"form": form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm()
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            return redirect('home')
    else:
        form = UserLoginForm()
    
    return render(request, 'django_registration/login.html', {"form": form})
        
def home(request):
    show_images = Image_Model.objects.all()
    context = {"images": show_images}
    return render(request, 'home/home.html', context)

def post(request):
    if request.method == 'POST':
        post_form = NewPostForm()
        if post_form.is_valid():
            image = post_form.cleaned_data['image']
            image_name = post_form.cleaned_data['image_name']
            image_caption = post_form.cleaned_data['image_caption']
            return HttpResponseRedirect('Image posted successfully')
    else:
        post_form = NewPostForm()
        
    return render(request, 'home/post.html', {"form": post_form})
    
def comment(request):
    if request.method == 'POST':
        comment_form = CommentForm()
        if comment_form.is_valid():
            comment = comment_form.cleaned_data['comment']
            return HttpResponseRedirect('Comment posted successfully')
    else:
       comment_form = CommentForm()
    
    return render(request, 'home/comment.html', {"form": comment_form})

def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm()
        if profile_form.is_valid():
            profile_picture = profile_form.cleaned_data['profile_picture']
            bio = profile_form = profile_form.cleaned_data['bio']
            return HttpResponseRedirect('Profile updated successfully')
    else:
        profile_form = ProfileForm()
        
    return render(request, 'profile/user.html', {"profile_form": profile_form})