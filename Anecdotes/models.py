from django.db import models
from django.shortcuts import reverse
import re
# from django.core.validators import MaxValueValidator


class Anecdote(models.Model):
    body = models.TextField(max_length=10000, unique=True, db_column='anecdote')
    source = models.TextField(max_length=100, blank=True, db_index=True, default='Unknown')
    creationdate = models.DateTimeField(db_index=True, auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='anecdotes', blank=True)

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse('anecdote_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('anecdote_update_url', kwargs={'id': self.id})

    def rate_update_url(self):
        return reverse('anecdote_detail_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('anecdote_delete_url', kwargs={'id': self.id})

    def get_votes(self):
        return Rates.objects.filter(anecdote=self.id).count()

    def get_rating(self):
        votes = self.get_votes()
        if votes > 0:
            return sum([r.rate for r in Rates.objects.filter(anecdote=self)]) / votes
        else:
            return 0

    def get_rate(self, user_object):
        rates = Rates.objects.filter(anecdote=self.id, user=user_object)
        return 0 if not rates.count() else rates[0].rate

    def canonize(self):
        reg = re.compile('[a-zA-Zа-яА-Я]+')
        return [x for x in reg.findall(self.body.lower()) if len(x) > 2]

    def gen_shingle(self, lgth=4):
        from binascii import crc32
        source = self.canonize()
        if len(source) < lgth:
            source += ["any"] * (lgth - len(source))
        return [crc32(' '.join([x for x in source[i:i + lgth]]).encode('utf-8')) for i in range(len(source)-lgth + 1)]

    class Meta:
        ordering = ['-id']


class Tag(models.Model):
    title = models.SlugField(max_length=50, unique=True, allow_unicode=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'id': self.id})

    class Meta:
        ordering = ['title']


class User(models.Model):
    user = models.SlugField(max_length=50, unique=True, db_index=True, allow_unicode=False)

    def __str__(self):
        return f"id: {self.id}, user: {self.user}"

    # def get_absolute_url(self):
    #      return reverse('users_list_url', kwargs={'id': self.id})

    class Meta:
        ordering = ['id']


class Rates(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_constraint=True)
    anecdote = models.ForeignKey('Anecdote', on_delete=models.CASCADE, db_constraint=True)
    rate = models.PositiveSmallIntegerField(max_length=None, unique=False, blank=False, null=False, db_index=True,
                                            editable=True, auto_created=False, validators=(), error_messages=None)

    def __str__(self):
        return f"ID: {self.id} Anecdote: {self.anecdote}, user: {self.user}, rate: {self.rate}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'anecdote'], name='unique_rating')
        ]
