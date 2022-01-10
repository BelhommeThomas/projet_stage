from django.contrib import admin
from .models import Affiliation, Fssbook, Participant
# Register your models here.
admin.site.register(Fssbook)
admin.site.register(Affiliation)
admin.site.register(Participant)