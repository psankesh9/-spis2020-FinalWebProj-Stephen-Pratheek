from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#Changing the default Django UserCreationForm by adding an Email field
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        #Changing the order the fields will be displayed in the registration form
        fields = ["username", "email", "password1", "password2"]