from django import forms
# from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import *
from .config import *
# from tools import *


class LegalFormForm(forms.ModelForm):
    class Meta:
        model = LegalForm
        fields = ['shortname', 'fullname', 'description']
        widgets = {
            'shortname': forms.TextInput(attrs=LARGE_ATTRS),
            'fullname': forms.TextInput(attrs=LARGE_ATTRS),
            'description': forms.Textarea(attrs=LARGE_ATTRS)
            }

    def clean_shortname(self):
        return self.cleaned_data['shortname']

    def clean_fullname(self):
        return self.cleaned_data['fullname']

    def clean_description(self):
        return self.cleaned_data['description']


class OrgForm(forms.ModelForm):
    class Meta:
        model = Org
        fields = ['fullname', 'lform', 'description']
        widgets = {
            'lform': forms.Select(attrs=LARGE_ATTRS),
            'fullname': forms.TextInput(attrs=LARGE_ATTRS),
            'description': forms.TextInput(attrs=LARGE_ATTRS),
            }

    def clean_fullname(self):
        return self.cleaned_data['fullname']

    def clean_description(self):
        return self.cleaned_data['description']


# class POSForm(forms.ModelForm):
#     class Meta:
#         model = PartOfSpeech
#         fields = ['rusname', 'engname', 'description']
#         widgets = {
#             'rusname': forms.TextInput(attrs=LARGE_ATTRS),
#             'engname': forms.TextInput(attrs=LARGE_ATTRS),
#             'description': forms.Textarea(attrs=LARGE_ATTRS)
#             }
#
#     def clean_rusname(self):
#         return self.cleaned_data['rusname']
#
#     def clean_engname(self):
#         return self.cleaned_data['engname']
#
#     def clean_description(self):
#         return self.cleaned_data['description']
#

# class HebrewRootForm(forms.ModelForm):
#
#     class Meta:
#         model = HebrewRoot
#         fields = ['root', 'ruswords']
#         help_texts = {
#             'ruswords': _('Input one or more russian words, separated by comma'),
#             }
#         widgets = {
#             'root': forms.TextInput(attrs=LARGE_ATTRS),
#             'ruswords': forms.TextInput(attrs=LARGE_ATTRS)
#             }
#
#     def clean_root(self):
#         return hebrew_letters_only(self.cleaned_data['root'])
#
#     def clean_ruswords(self):
#         return self.cleaned_data['ruswords']
#
#
# class ThemeForm(forms.ModelForm):
#     class Meta:
#         model = Theme
#         fields = ['rusname', 'engname', 'description']
#         widgets = {
#             'rusname': forms.TextInput(attrs=LARGE_ATTRS),
#             'engname': forms.TextInput(attrs=LARGE_ATTRS),
#             'description': forms.Textarea(attrs=LARGE_ATTRS)
#             }
#
#     def clean_rusname(self):
#         return clean_phrase(self.cleaned_data['rusname'])
#
#     def clean_engname(self):
#         return clean_phrase(self.cleaned_data['engname'])
#
#     def clean_description(self):
#         return self.cleaned_data['description']
#
#
# class PrepositionForm(forms.ModelForm):
#     class Meta:
#         model = Preposition
#         fields = ['hword', 'hword_with_cons', 'ruswords', 'pronunciation', 'type', 'description']
#         widgets = {
#             'hword': forms.TextInput(attrs=LARGE_ATTRS),
#             'hword_with_cons': forms.TextInput(attrs=LARGE_ATTRS),
#             'pronunciation': forms.TextInput(attrs=LARGE_ATTRS),
#             'type': forms.Select(attrs=LARGE_ATTRS),
#             'ruswords': forms.SelectMultiple(attrs=LARGE_ATTRS),
#             'description': forms.Textarea(attrs=LARGE_ATTRS),
#         }
#
#     def clean_hword(self):
#         return self.cleaned_data['hword']
#
#     def clean_hword_with_cons(self):
#         return self.cleaned_data['hword_with_cons']
#
#     def clean_pronunciation(self):
#         return self.cleaned_data['pronunciation']
#
#     def clean_description(self):
#         return self.cleaned_data['description']
#
#
# class PronounForm(forms.ModelForm):
#     class Meta:
#         model = Pronoun
#         fields = ['hword', 'hword_with_cons', 'ruswords', 'pronunciation', 'gender', 'number', 'description']
#         widgets = {
#             'hword': forms.TextInput(attrs=LARGE_ATTRS),
#             'hword_with_cons': forms.TextInput(attrs=LARGE_ATTRS),
#             'pronunciation': forms.TextInput(attrs=LARGE_ATTRS),
#             'gender': forms.Select(attrs=LARGE_ATTRS),
#             'number': forms.Select(attrs=LARGE_ATTRS),
#             'ruswords': forms.SelectMultiple(attrs=LARGE_ATTRS),
#             'description': forms.Textarea(attrs=LARGE_ATTRS)
#         }
#
#     def clean_hword(self):
#         return self.cleaned_data['hword']
#
#     def clean_hword_with_cons(self):
#         return self.cleaned_data['hword_with_cons']
#
#     def clean_pronunciation(self):
#         return self.cleaned_data['pronunciation']
#
#     def clean_description(self):
#         return self.cleaned_data['description']
#
#
