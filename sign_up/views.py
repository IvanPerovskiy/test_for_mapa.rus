from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Topic
from .forms import TopicForm, LoginForm, UserRegistrationForm



# Create your views here.
def index(request):
    return render(request, 'sign_up/index.html')

def register(request):

    if request.method != 'POST':
    # Display blank registration form.
        form = UserCreationForm()
    else:
    # Обработка заполненной формы.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
    # Выполнение входа и перенаправление на домашнюю страницу.
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('sign_up:index'))
    context = {'form': form}
    return render(request, 'sign_up/register.html', context)


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'sign_up/topics.html', context)

def new_topic(request):

    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sign_up:topics'))
    context = {'form': form}
    return render(request, 'sign_up/new_topic.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('sign_up/index/')
                else:
                    return render(request,
                                  'sign_up/disabled_password.html')
            else:
                return render(request,
                              'sign_up/disabled_password.html')
    else:
        form = LoginForm()
    return render(request, 'sign_up/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()

            return HttpResponseRedirect('/sign_up/login/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'sign_up/register.html', {'user_form': user_form})

def register(request):
    if request.method != 'POST':
        form = UserRegistrationForm()
    else:
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username,
            password=request.POST['password1'])
            login(request, authenticated_user)
        return HttpResponseRedirect(reverse('sign_up:index'))
    context = {'form': form}
    return render(request, 'sign_up/register.html', context)