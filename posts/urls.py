# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path(r'', views.top, name='top'),
    path(r'create/', views.create, name='create'),
    path(r'confirm/', views.confirm, name='confirm'),
    path(r'save/', views.save, name='save'),
    path(r'<int:post_id>/', views.detail, name='detail'),
    path(r'reply/create/', views.reply_create, name='reply-create'),
]
