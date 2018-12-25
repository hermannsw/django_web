# -*- coding: utf-8 -*-

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Reply(models.Model):
    body = models.TextField(max_length=1000)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
