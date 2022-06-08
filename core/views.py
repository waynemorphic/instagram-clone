from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from core.forms import UserLoginForm, UserRegistrationForm, CommentForm, NewPostForm, ProfileForm, NewsLetterForm
from core.models import User_Model, Profile_Model, Image_Model, NewsLetterRecipients
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from core.email import send_welcome_email

# Create your views here.

# index function to render index template file
def index(request):
    return render(request, 'home/index.html')



def logout_user(request):
    logout(request)
    return render(request, 'home/index.html')

@login_required(login_url = 'accounts/login/')
def home(request):
    show_images = Image_Model.objects.all()
    user_profile = Profile_Model.objects.all()
    if request.method == 'POST':
        sub_form = NewsLetterForm(request.POST)
        if sub_form.is_valid():
            name = sub_form.cleaned_data['your_name']
            email = sub_form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name, email)
            HttpResponseRedirect('home')
    else:
        sub_form = NewsLetterForm()
    context = {"show_images": show_images, "user_profile": user_profile, "sub_form": sub_form}
    return render(request, 'home/home.html', context)

@login_required(login_url = 'accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        post_form = NewPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_image = post_form.save(commit = False)
            User_Model.user = current_user
            new_image.save()
            print('new_image')
            
            return redirect('home/')
    else:
        post_form = NewPostForm()
        
    return render(request, 'home/post.html', {"form": post_form})

@login_required(login_url = 'accounts/login/')  
def comment(request):
    current_user = request.user
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = True)
            User_Model.username = current_user
            new_comment.save()
            return redirect('home/')
    else:
       comment_form = CommentForm()
    
    return render(request, 'home/comment.html', {"comment_form": comment_form})

def profile(request):
    all_pictures = Image_Model.objects.all()
    user_profile = Profile_Model.objects.all()
    return render(request,'profile/user.html', {"all_pictures": all_pictures, "user_profile": user_profile})


@login_required(login_url = 'accounts/login/')  
def update_profile(request):    
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile_picture = profile_form.save(commit = False)
            bio = profile_form.cleaned_data['bio']
            profile_picture = profile_form.cleaned_data['profile_photo']
            profile_form.bio = bio
            profile_form.profile_picture = profile_picture
            profile_form.save()
            print(profile_form)
            return redirect('profile')
    else:
        profile_form = ProfileForm()
        
    return render(request, 'profile/update_profile.html', {"profile_form": profile_form})

def search_results(request):
    if 'pic' in request.GET and request.GET['pic']:
        search_term = request.GET.get("pic")
        searched_pic = Image_Model.search_image(search_term)
        message = f'{search_term}'
        return render(request, 'home/search.html', {"message": message, "pics": searched_pic})
    else:
        message='You have not searched for any image'
    return render(request, 'home/search.html', {"message": message})

def delete_stuff(request):
    delete = Image_Model.delete_image()
    remove = Profile_Model.objects.delete()
    context = {"delete": delete, "remove": remove}
    return render(request, 'profile/user.html', context)