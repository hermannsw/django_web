# -*- coding: utf-8 -*-

import facebook
from django.contrib.auth.models import Group

from users.models import User


def save_email(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        graph = facebook.GraphAPI(access_token=response['access_token'], version="2.7")
        saved_user = User.objects.get(pk=user.id)
        email = graph.get_object(id=response['id'], fields="email")
        saved_user.email = email['email']
        saved_user.save()

def add_group(backend, user, response, *args, **kwards):
    user.groups.add(Group.objects.get(name='general'))
