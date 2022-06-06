from email.mime import image
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from core.forms import UserLoginForm, UserRegistrationForm, CommentForm, NewPostForm, ProfileForm
from core.models import User_Model, Profile_Model, Image_Model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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
            print(form)
            return redirect('home')
            
    else:
        form = UserRegistrationForm()
        
    return render(request, 'django_registration/registration.html', {"form": form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email = email, password = password)
        print(form)
        if form.is_valid() and user is not None:
            login(request, user)
            login_user = form.save(commit = True)
            login_user.save()
            return redirect('home/home.html')
    else:
        form = UserLoginForm()
    
    return render(request, 'django_registration/login.html', {"form": form})


def logout_user(request):
    logout(request)
    return render(request, 'home/index.html')


def home(request):
    show_images = Image_Model.objects.all()
    context = {"show_images": show_images}
    return render(request, 'home/home.html', context)

@login_required(login_url = 'accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        post_form = NewPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = current_user
            new_post.save()
            # image = post_form.cleaned_data['image']
            # image_name = post_form.cleaned_data['image_name']
            # image_caption = post_form.cleaned_data['image_caption']
            return redirect('home')
    else:
        post_form = NewPostForm()
        
    return render(request, 'home/post.html', {"form": post_form})

@login_required(login_url = 'accounts/login/')  
def comment(request):
    current_user = request.user
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit = True)
            comment_form.user = current_user
            comment_form.save()
            return redirect('home')
    else:
       comment_form = CommentForm()
    
    return render(request, 'home/comment.html', {"form": comment_form})

@login_required(login_url = 'accounts/login/')  
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_picture = profile_form.save(commit = False)
            profile_form.user = current_user
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm()
        
    return render(request, 'profile/user.html', {"profile_form": profile_form})