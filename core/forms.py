
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
    
class NewPostForm(forms.Form):
    image = forms.ImageField(label = 'Upload Image')
    image_name = forms.CharField(label = 'Image Name', max_length=50)
    image_caption = forms.CharField(label = 'Image Caption', max_length = 100)

class CommentForm(forms.Form):
    comments = forms.CharField(widget = forms.Textarea)

class ProfileForm(forms.Form):
    profile_picture = forms.ImageField(label = 'Upload Profile Picture')
    bio = forms.Textarea()