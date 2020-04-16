from django.db import models
# from django.urls import reverse
from django.db.models import Q
from .hebrew_symbols import *


class Binyan(models.Model):
    hebname = models.CharField(max_length=10, unique=True)
    rusname = models.SlugField(max_length=10, unique=True, allow_unicode=True)
    description = models.TextField(max_length=None, unique=False, blank=True, default='', editable=True)
    scheme = models.ImageField(blank=True, upload_to='polyglot/')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.hebname}, {self.rusname}"

    def get_absolute_url(self):
        return reverse('binyan_details_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('binyan_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('binyan_delete_url', kwargs={'id': self.id})


class PartOfSpeech(models.Model):
    rusname = models.SlugField(max_length=16, unique=True, allow_unicode=True)
    engname = models.SlugField(max_length=16, unique=True)
    description = models.TextField(max_length=None, unique=False, blank=True, default='', editable=True)

    class Meta:
        ordering = ['rusname']

    def __str__(self):
        return f"{self.rusname}"

    def get_absolute_url(self):
        return reverse('pos_details_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('pos_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('pos_delete_url', kwargs={'id': self.id})


class RusWord(models.Model):
    word = models.CharField(max_length=100, unique=True)
    pos = models.ForeignKey('PartOfSpeech', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.word}"

    def get_absolute_url(self):
        return reverse('rusword_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('rusword_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('rusword_delete_url', kwargs={'id': self.id})

    class Meta:
        ordering = ['word']


class HebrewRoot(models.Model):
    root = models.CharField(max_length=5, unique=True)
    ruswords = models.ManyToManyField('RusWord', related_name='hebrewroots')

    def __str__(self):
        return f"{self.root}"

    def get_absolute_url(self):
        return reverse('hebrewroot_details_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('hebrewroot_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('hebrewroot_delete_url', kwargs={'id': self.id})

    def dotroot(self):
        return '.'.join(list(self.root))

    class Meta:
        ordering = ['root']


class Theme(models.Model):
    rusname = models.CharField(max_length=32, unique=True)
    engname = models.CharField(max_length=32, blank=True)
    description = models.TextField(max_length=None, unique=False, blank=True)

    class Meta:
        ordering = ['rusname']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = None

    def __str__(self):
        return f"{self.rusname}"

    def get_absolute_url(self):
        return reverse('theme_details_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('theme_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('theme_delete_url', kwargs={'id': self.id})


class Preposition(models.Model):
    prep_object = PartOfSpeech.objects.get(engname='preposition')
    particle_object = PartOfSpeech.objects.get(engname='particle')
    Type = models.IntegerChoices('Type', 'FIRST SECOND EXCEPTION UNKNOWN')
    pre_choice = Q(pos=prep_object.id) | Q(pos=particle_object.id)
    hword = models.CharField(max_length=20, unique=True)
    hword_with_cons = models.CharField(max_length=50, unique=False, blank=False)
    ruswords = models.ManyToManyField('RusWord', limit_choices_to=pre_choice)
    pronunciation = models.CharField(max_length=20, unique=False, blank=True)
    type = models.SmallIntegerField(choices=Type.choices)
    description = models.TextField(max_length=1000, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.hword)
        self.hword_cons = remove_niqqud_from_last_letter(self.hword_with_cons)

    class Meta:
        ordering = ['hword']

    def __str__(self):
        return f"{self.hword}: {self.ruswords}"

    def get_absolute_url(self):
        return reverse('prep_details_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('prep_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('prep_delete_url', kwargs={'id': self.id})

    def single_first(self):
        if self.type == 1:
            res = self.hword_cons + chr(1460) + chr(1497)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1460) + chr(1502) + chr(1462) + chr(1504) + chr(1497)
        else:
            res = ''
        return res

    def single_second_male(self):
        if self.type == 1:
            res = self.hword_cons + chr(1461) + chr(1498) + chr(1464)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1460) + chr(1502) + chr(1456) + chr(1498) + chr(1464)
        else:
            res = ''
        return res

    def single_second_female(self):
        if self.type == 1:
            res = self.hword_cons + chr(1464) + chr(1498) + chr(1456)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1460) + chr(1502) + chr(1462) + chr(1498) + chr(1456)
        else:
            res = ''
        return res

    def single_third_male(self):
        if self.type == 1:
            res = self.hword_cons + chr(1493) + chr(1465)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1460) + chr(1502) + chr(1462) + chr(1504) + chr(1493) + chr(1465)
        else:
            res = ''
        return res

    def single_third_female(self):
        if self.type == 1:
            res = self.hword_cons + chr(1464) + chr(1492) + chr(1468)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1460) + chr(1502) + chr(1462) + chr(1504) + chr(1464) + chr(1492)
        else:
            res = ''
        return res

    def plural_first(self):
        if self.type == 1:
            res = self.hword_cons + chr(1464) + chr(1504) + chr(1493) + chr(1468)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1488) + chr(1460) + chr(1497) + chr(1514) + chr(1463) + chr(1504) + chr(1493) + chr(1468)
        else:
            res = ''
        return res

    def plural_second_male(self):
        if self.type == 1:
            res = self.hword_cons + chr(1464) + chr(1499) + chr(1462) + chr(1501)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1460) + chr(1499) + chr(1462) + chr(1501)
        else:
            res = ''
        return res

    def plural_second_female(self):
        if self.type == 1:
            res = self.hword_cons + chr(1464) + chr(1499) + chr(1462) + chr(1503)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1460) + chr(1499) + chr(1462) + chr(1503)
        else:
            res = ''
        return res

    def plural_third_male(self):
        if self.type == 1:
            res = self.hword_cons + chr(1464) + chr(1492) + chr(1462) + chr(1501)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1460) + chr(1492) + chr(1462) + chr(1501)
        else:
            res = ''
        return res

    def plural_third_female(self):
        if self.type == 1:
            res = self.hword_cons + chr(1464) + chr(1492) + chr(1462) + chr(1503)
        elif self.type == 2:
            res = ''
        elif self.hword == 'מ':
            res = chr(1502) + chr(1460) + chr(1492) + chr(1462) + chr(1503)
        else:
            res = ''
        return res


class Pronoun(models.Model):
    pos_object = PartOfSpeech.objects.get(engname='pronoun')
    Gender = models.TextChoices('Gender', 'Male Female Irrelevant')
    Number = models.TextChoices('Number', 'Singular Plural Irrelevant')
    pre_choice = Q(pos=pos_object.id)
    hword = models.CharField(max_length=20, unique=False)
    hword_with_cons = models.CharField(max_length=50, unique=False, blank=True)
    ruswords = models.ManyToManyField('RusWord', limit_choices_to=pre_choice)
    pronunciation = models.CharField(max_length=20, unique=False, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    number = models.CharField(max_length=10, choices=Number.choices)
    description = models.TextField(max_length=1000, blank=True)

    class Meta:
        ordering = ['hword']
        constraints = [
            models.UniqueConstraint(fields=['hword', 'hword_with_cons', 'gender', 'number'], name='unique_pronoun')
        ]

    def __str__(self):
        return f"{self.hword}: {self.ruswords}"

    def get_absolute_url(self):
        return reverse('pron_details_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('pron_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('pron_delete_url', kwargs={'id': self.id})



# class HebrewWord(models.Model):
#     hword = models.CharField(max_length=20, unique=True)
#     pronunciation = models.CharField(max_length=20, unique=True, blank=True)
#     ruswords = models.ManyToManyField('RusWord', related_name='hwords')
#     root = models.ForeignKey('HebrewRoot', on_delete=models.CASCADE, related_name=None)
#     p_of_speech = models.ForeignKey('PartOfSpeech', on_delete=models.CASCADE, related_name=None)
#     themes = models.ManyToManyField('Theme', related_name='hwords')
#
#     def __str__(self):
#         return f"{self.root}"
#
#     def get_absolute_url(self):
#         return reverse('hword_detail_url', kwargs={'id': self.id})
#
#     def get_update_url(self):
#         return reverse('hword_update_url', kwargs={'id': self.id})
#
#     def get_delete_url(self):
#         return reverse('hword_delete_url', kwargs={'id': self.id})
#
#     class Meta:
#         ordering = ['hword']
#
#
# class HebrewPhrase(models.Model):
#     hphrase = models.CharField(max_length=100, unique=True)
#     # pronunciation = models.SlugField(max_length=20, unique=True, allow_unicode=True, blank=True)
#     ruswords = models.ManyToManyField('RusWord', related_name='hphrases')
#
#     def __str__(self):
#         return f"{self.hphrase}"
#
#     def get_absolute_url(self):
#         return reverse('hphrase_detail_url', kwargs={'id': self.id})
#
#     def get_update_url(self):
#         return reverse('hphrase_update_url', kwargs={'id': self.id})
#
#     def get_delete_url(self):
#         return reverse('hphrase_delete_url', kwargs={'id': self.id})
#
#     class Meta:
#         ordering = ['hphrase']
#

# class HebrewSymbol(models.Model):
#     # id equal the utf8 code
#     id = models.PositiveSmallIntegerField(unique=True, primary_key=True, auto_created=False, serialize=False)
#     rusname = models.SlugField(max_length=16, unique=True, allow_unicode=True)
#     hebname = models.SlugField(max_length=16, unique=True, allow_unicode=True)
#     engname = models.SlugField(max_length=16, unique=True)
#     sofit = models.BooleanField(blank=False, null=False,  default=False, choices=None, auto_created=False)
#     dagesh = models.BooleanField(blank=False, null=False,  default=False, choices=None, auto_created=False)
#     description = models.TextField(max_length=None, unique=False, blank=True, default='', editable=True)
#
#     class Meta:
#         ordering = ['id']
#
#     def __str__(self):
#         return f"{self.rusname}"
#
#     def get_absolute_url(self):
#         return reverse('symbol_details_url', kwargs={'id': self.id})
