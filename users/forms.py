# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django_web.classes.areacode import AreaCode


class GeneralUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class GeneralUserDetailForm(forms.Form):

    choices = AreaCode.all_tuple()

    first_name = forms.CharField()
    last_name = forms.CharField()
    birthed_at = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}), input_formats='%Y-%m-%d')
    residence = forms.ChoiceField(label='居住地', widget=forms.Select, choices=choices,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        fields = ('first_name', 'last_name', 'birthed_at', 'residence')


class AgentCreationForm(GeneralUserCreationForm):
    is_career_consultant = forms.BooleanField()
