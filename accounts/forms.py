from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'first_name', 'last_name', 'tel', 'profile_pic', 'password1', 'password2')
    