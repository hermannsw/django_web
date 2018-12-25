# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'django_web/index.html', context)
