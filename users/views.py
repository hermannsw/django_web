# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from users.forms import AgentCreationForm, GeneralUserCreationForm

from .models import Agent, User


def signup(request):
    form = GeneralUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)


@require_http_methods(['POST'])
def confirm(request):
    form = GeneralUserCreationForm(request.POST)
    if form.is_valid():
        request.session['username'] = request.POST['username']
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password1']
        context = {
            'username': request.session['username'],
            'email': request.session['email'],
            'password': request.session['password']
        }
        return render(request, 'users/confirm.html', context)
    else:
        context = {
            'form': form
        }
        return render(request, 'users/signup.html', context)


@require_http_methods(['POST'])
def create(request):
    created_user = User.objects.create_user(
        username=request.session['username'],
        email=request.session['email'],
        password=request.session['password']
    )
    created_user.groups.add(Group.objects.get(name='general'))
    return HttpResponseRedirect('/mypage')


def agent_signup(request):
    form = AgentCreationForm()
    context = {
        'form': form
    }
    return render(request, 'users/agent/signup.html', context)


@require_http_methods(['POST'])
def agent_confirm(request):
    form = GeneralUserCreationForm(request.POST)
    if form.is_valid():
        request.session['username'] = request.POST['username']
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password1']
        context = {
            'username': request.session['username'],
            'email': request.session['email'],
            'password': request.session['password']
        }
        return render(request, 'users/agent/confirm.html', context)
    else:
        return HttpResponseRedirect('/users/agent/signup')


@require_http_methods(['POST'])
def agent_create(request):
    created_user = Agent.objects.create_user(
        username=request.session['username'],
        email=request.session['email'],
        password=request.session['password']
    )
    created_user.groups.add(Group.objects.get(name='agent'))
    return HttpResponseRedirect('/')
