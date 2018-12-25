# -*- coding: utf-8 -*-

from django.urls import path

from . import views

app_name = 'mypage'
urlpatterns = [
    path(r'', views.top, name='top'),
    path(r'edit/', views.edit, name='edit'),
    path(r'edit/save', views.edit_save, name='edit-save')
]
