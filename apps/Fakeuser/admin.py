from django.contrib import admin

# Register your models here.
from .models import Fakeuser

@admin.register(Fakeuser)
class FakeuserAdmin(admin.ModelAdmin):
    list_display = ['name','gender','email','address','phone','job','live_city','married','language','latutude','longitude','username','password','image']