from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Topic


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput)
    #password = forms.CharField(label='sddsPassword', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','last_name','email')

