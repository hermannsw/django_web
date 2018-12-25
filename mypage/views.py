# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from users.forms import GeneralUserDetailForm
from users.models import User


@login_required
def top(request):
    login_user = request.user
    login_user_detail = login_user.userdetail_set.first()
    group = login_user.groups.get()
    if group.name == 'general':
        image_url = 'https://s3-ap-northeast-1.amazonaws.com/dev-django_web/users/no_image.jpg'
        posts = login_user.posts.all()
        context = {
            'title': 'マイページ',
            'user': login_user,
            'image_url': image_url,
            'detail': login_user_detail,
            'posts': posts
        }
        return render(request, 'mypage/user/top.html', context)


@login_required
def edit(request):
    user_data = {}
    if request.user.userdetail_set.exists():
        user_detail = request.user.userdetail_set.first()
        user_data = {
            'last_name': request.user.last_name,
            'first_name': request.user.first_name,
            'birthed_at': user_detail.birthed_at,
            'residence': user_detail.residence,
        }
    else:
        user_data = {
            'last_name': request.user.last_name,
            'first_name': request.user.first_name
        }
    form = GeneralUserDetailForm(user_data)
    image_url = 'https://s3-ap-northeast-1.amazonaws.com/dev-coqoon/users/no_image.jpg'
    context = {
        'form': form,
        'image_url': image_url
    }
    return render(request, 'mypage/user/edit.html', context)


def edit_save(request):
    user = User.objects.filter(pk=request.user.id).first()
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()
    if user.userdetail_set.exists() is True:
        detail = user.userdetail_set.first()
        detail.birthed_at = request.POST['birthed_at']
        detail.residence = request.POST['residence']
        detail.save()
    else:
        user.userdetail_set.create(
            birthed_at=request.POST['birthed_at'],
            residence=request.POST['residence']
        )
    return HttpResponseRedirect('/mypage')
