from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.model_translation.models import Words


@admin.register(Words)
class WordsAdmin(TranslationAdmin):
    list_display = ('word', 'definition')

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
