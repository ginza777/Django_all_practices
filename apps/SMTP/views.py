#email
from django.shortcuts import render

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'https://mail.tuit.uz/'
EMAIL_HOST_USER = 'ginza@tuit.uz'
EMAIL_HOST_PASSWORD = 'v56QbUS9'
RECEIPT_EMAIL = 'ondayevsanat@gmail.com'

from django.core.mail import EmailMessage, get_connection


def send_email(request):
    if request.method == "POST":
        subject = "Привет!"
        message = "Привет, это тестовое письмо."
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=EMAIL_HOST_USER,
            to=[RECEIPT_EMAIL],
        )
        email.send()
    return render(request, 'email.html')
