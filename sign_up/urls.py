from django.conf.urls import url
from django.contrib.auth.views import auth_login
#from django.urls import path
from . import views
urlpatterns = [
    url(r'^login/$', views.user_login,name='login'),
    url(r'^logout/$', views.user_logout,name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^policy/$', views.policy, name='policy'),


]