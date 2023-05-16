from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Words(models.Model):
    word= models.CharField(_('word'),max_length=100,blank=True)
    definition = models.TextField(_('definition'),blank=True)
    language= models.CharField(max_length=10,blank=True,default='en')

    def __str__(self):
        return self.word

    class Meta:
        db_table = 'Modeltranslation'
        verbose_name_plural = _('Modeltranslation_words')
