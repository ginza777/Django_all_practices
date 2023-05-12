from django.contrib import admin
from .models import Company, Vacancies, Clients, Resume


# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'logo', 'description')


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'salary', 'company')


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'phone', 'username', 'password', 'email', 'image')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'resume')
