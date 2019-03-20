from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUser


class LoginForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email','class' : 'myfield'}), required=True)
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password','class' : 'myfield'}), required=True)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'First name', 'class' : 'myfield'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Last name','class' : 'myfield'}),required=True)
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class' : 'myfield'}),required=True)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password','class' : 'myfield'}),required=True)
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password','class' : 'myfield'}))
    newsletter = forms.BooleanField(required=False,label="I'd like to receive PlacePass news and offers",
                                    widget=forms.CheckboxInput(attrs={'checked':''}))

    class Meta:
        model = MyUser
        fields = ('first_name','last_name','email','password1','password2','newsletter')



