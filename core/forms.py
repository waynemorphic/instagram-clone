from django import forms

class UserRegistrationForm(forms.Form):
    email = forms.EmailField(label = 'Email', required = True)
    full_name = forms.CharField(label= 'Full Name', min_length = 4, required= True)
    username = forms.CharField(label = 'Username', required = True)
    password = forms.CharField(label = 'Password', required = True)
    
class UserLoginForm(forms.Form):
    email = forms.EmailField(label = 'Email', required = True)
    password = forms.CharField(label = 'Password', required = True)