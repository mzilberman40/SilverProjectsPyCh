from django import forms
from django.core.exceptions import ValidationError
from .models import *
# from tools import *


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
            }

    def clean_title(self):
        return self.cleaned_data['title'].lower()


class AnecdoteForm(forms.ModelForm):
    class Meta:
        model = Anecdote
        fields = ['body', 'source', 'tags']
        widgets = {
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
            }

    def clean_body(self):
        return self.cleaned_data['body']

    def clean_source(self):
        return self.cleaned_data['source']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            }

    def clean_user(self):
        return self.cleaned_data['user']


class RatesForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ['user', 'anecdote', 'rate']
        widgets = {
            'rate': forms.NumberInput(attrs={'class': 'form-control'})
            }

    def clean_rate(self):
        rate = self.cleaned_data['rate']
        try:
            rate = int(rate)
        except ValueError:
            raise ValidationError("Rate has to be integer", code=None, params=None)
        if rate < 0 or rate > 10:
            raise ValidationError("Rate has to be integer between 0 and 10", code=None, params=None)

        return rate
