# -*- coding: utf-8 -*-

from django import forms

from .models import Post, Reply


class PostForm(forms.ModelForm):
    CHOICES = [('True', '公開'), ('False', '非公開')]
    is_public = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Post
        fields = ('title', 'body', 'is_public')
        widgets = {
            'title': forms.TextInput(attrs={'size': 40}),
            'body': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class ReplyForm(forms.ModelForm):
    CHOICES = [('True', '公開'), ('False', '非公開')]
    is_public = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Reply
        fields = ('body', 'is_public')
