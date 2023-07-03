#email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'geenzaofficial@gmail.com'
EMAIL_HOST_PASSWORD = 'sherzAmon2001A'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER