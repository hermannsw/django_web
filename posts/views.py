# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from users.models import User

from .forms import PostForm, ReplyForm
from .models import Post, Reply


@login_required
def top(request):
    posts = Post.objects.filter(is_public=True)
    contents = []
    for p in posts:
        user = p.user_set.first()
        contents.append({'post': p, 'user': user})
    context = {
        'contents': contents
    }
    return render(request, 'posts/post/top.html', context)


@login_required
def create(request):
    context = {
        'form': PostForm
    }
    return render(request, 'posts/post/create.html', context)


@require_http_methods(['POST'])
def confirm(request):
    form = PostForm(request.POST)
    if form.is_valid():
        request.session['title'] = request.POST['title']
        request.session['body'] = request.POST['body']
        request.session['is_public'] = request.POST['is_public']
        context = {
            'title': request.session['title'],
            'body': request.session['body'],
            'is_public': request.session['is_public']
        }
        return render(request, 'posts/post/confirm.html', context)
    else:
        return HttpResponseRedirect('posts:create')


@require_http_methods(['POST'])
def save(request):
    created_post = Post.objects.create(
        title=request.session['title'],
        body=request.session['body'],
        is_public=request.session['is_public']
    )
    user = User.objects.get(pk=request.user.id)
    user.posts.add(created_post.id)
    return HttpResponseRedirect('/posts/')


def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    replies = []
    for r in post.reply_set.filter(is_public=True):
        replies.append({'reply': r, 'user': r.user_set.first()})
    form = ReplyForm()
    context = {
        'post': post,
        'replies': replies,
        'form': form
    }
    return render(request, 'posts/post/detail.html', context)


def reply_create(request):
    created_reply = Reply.objects.create(
        body=request.POST['body'],
        is_public=request.POST['is_public'],
        post_id=request.POST['post_id']
    )
    user = User.objects.get(pk=request.user.id)
    user.replies.add(created_reply)
    return HttpResponseRedirect('/posts/' + request.POST['post_id'])
