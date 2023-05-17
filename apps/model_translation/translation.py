from apps.model_translation.models import Words
from modeltranslation.translator import TranslationOptions, register


@register(Words)
class WordsTranslationOptions(TranslationOptions):
    fields = ('word', 'definition')
