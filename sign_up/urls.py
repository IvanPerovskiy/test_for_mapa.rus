from django.conf.urls import url
from django.contrib.auth.views import auth_login
#from django.urls import path
from . import views
urlpatterns = [
    url(r'^login/$', views.user_login,name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
]