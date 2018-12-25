# -*- coding: utf-8 -*-

from django.contrib.auth.views import login, logout
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path(r'signup/', views.signup, name='signup'),
    path(r'confirm/', views.confirm, name='confirm'),
    path(r'create/', views.create, name='create'),
    path(r'login/', login, {'template_name': 'users/login.html'}, name='login'),
    path(r'logout/', logout, name='logout'),
    path(r'agent/signup/', views.agent_signup, name='agent-signup'),
    path(r'agent/confirm/', views.agent_confirm, name='agent-confirm'),
    path(r'agent/create/', views.agent_create, name='agent-create'),
]
