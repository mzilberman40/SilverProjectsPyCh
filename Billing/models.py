from django.db import models
from django.shortcuts import reverse


class LegalForm(models.Model):
    shortname = models.SlugField(max_length=10, unique=True, allow_unicode=True)
    fullname = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.shortname}"

    def get_absolute_url(self):
        return reverse('lform_details_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('lform_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('lform_delete_url', kwargs={'id': self.id})

    class Meta:
        ordering = ['shortname']


class Org(models.Model):
    fullname = models.CharField(max_length=100, unique=False)
    lform = models.ForeignKey('LegalForm', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.lform}  {self.fullname}"

    def get_absolute_url(self):
        return reverse('org_details_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('org_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('org_delete_url', kwargs={'id': self.id})

    class Meta:
        ordering = ['fullname']


class Person(models.Model):
    firstname = models.SlugField(max_length=20, unique=False, allow_unicode=True, blank=True)
    lastname = models.SlugField(max_length=20, unique=False, allow_unicode=True, db_index=True,  blank=True)
    middlename = models.SlugField(max_length=20, unique=False, allow_unicode=True,  blank=True)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.lastname},  {self.firstname}"

    def get_absolute_url(self):
        return reverse('person_details_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('person_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('person_delete_url', kwargs={'id': self.id})

    class Meta:
        ordering = ['lastname']
