from django.contrib import admin
from .models import *


@admin.register(Words)
class RossettaAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'definition', 'language')
# Register your models here.
