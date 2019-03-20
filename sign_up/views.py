from mysite import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, UserRegistrationForm
from django.core.mail import send_mail
from django.template.loader import render_to_string



# Create your views here.
def index(request):
    return render(request, 'sign_up/index.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/sign_up')
                else:
                    return render(request,
                                  'sign_up/wrong_password.html')
            else:
                return render(request,
                              'sign_up/wrong_password.html')
    else:
        form = LoginForm()
    return render(request, 'sign_up/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/sign_up')

def register(request):
    if request.method != 'POST':
        form = UserRegistrationForm()
    else:

        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            data = request.POST
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.email,
            password=request.POST['password1'])

            login(request, authenticated_user)
            try:
                newsletter = data['newsletter']
                email = data['email']
                if newsletter:
                    subject = 'Registration'
                    message = render_to_string('sign_up/message.html')
                    send_mail(subject, message, settings.EMAIL_HOST_USER, [email])
            except:
                pass

            return HttpResponseRedirect('/sign_up')
    context = {'form': form}
    return render(request, 'sign_up/register.html', context)

def terms(request):
    return render(request, 'sign_up/terms.html')

def policy(request):
    return render(request, 'sign_up/policy.html')
