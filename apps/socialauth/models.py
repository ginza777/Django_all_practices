from django.db import models

# Create your models here.

class SocialAuthUser(models.Model):
    user_id = models.IntegerField()
    provider = models.CharField(max_length=255)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'social_auth_users'
        verbose_name = 'Social Auth User'
        verbose_name_plural = 'Social Auth Users'
    def __str__(self):
        return self.user_id