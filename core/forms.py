
from django import forms
from core.models import User_Model, Profile_Model, Image_Model


class UserRegistrationForm(forms.Form):
    email = forms.EmailField(label = 'Email', required = True)
    full_name = forms.CharField(label= 'Full Name', min_length = 4, required= True)
    username = forms.CharField(label = 'Username', required = True)
    password = forms.CharField(label = 'Password', required = True)
    
class UserLoginForm(forms.Form):
    email = forms.EmailField(label = 'Email', required = True)
    password = forms.CharField(label = 'Password', required = True)
    
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image_Model
        exclude = ['user', 'post_date', 'likes', 'comments', 'profile']
  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Image_Model
        exclude = ['image','image_name','image_caption','user', 'post_date', 'likes', 'profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile_Model
        exclude = ['user']
    
    
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')