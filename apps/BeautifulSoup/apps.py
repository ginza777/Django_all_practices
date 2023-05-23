from django.apps import AppConfig
from .views import *

class BeautifulsoupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.BeautifulSoup'

