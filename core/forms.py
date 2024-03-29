from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class loginform(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username','class': 'w-full py-4 px-6 rounded-xl'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class': 'w-full py-4 px-6 rounded-xl'}))
      
class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1')
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your username','class': 'w-full py-4 px-6 rounded-xl'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email','class': 'w-full py-4 px-6 rounded-xl'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class': 'w-full py-4 px-6 rounded-xl'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password again','class': 'w-full py-4 px-6 rounded-xl'}))



        