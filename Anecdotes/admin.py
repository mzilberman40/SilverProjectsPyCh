from django.contrib import admin
from .models import *

admin.site.register(Anecdote)
admin.site.register(Tag)
admin.site.register(User)
admin.site.register(Rates)
