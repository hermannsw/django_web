# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from posts.models import Post, Reply


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    posts = models.ManyToManyField(Post)
    replies = models.ManyToManyField(Reply)


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthed_at = models.DateField(null=True)
    residence = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Agent(User):
    is_career_consultant = models.BooleanField(default=False)
