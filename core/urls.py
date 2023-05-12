from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("befitapp/", include("apps.befit.urls")),
    path("vacancyapp/", include("apps.vacancy.urls")),
    path("captchaapp/", include("apps.app_captcha.urls")),
    path("user/", include("apps.backendfilter.urls")),

]
urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
