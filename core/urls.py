from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include,re_path
from .schema import swagger_urlpatterns

urlpatterns = [
    re_path(r'^rosetta/', include('rosetta.urls')),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("apps.authentication.urls")),
    path("befitapp/", include("apps.befit.urls")),
    path("vacancyapp/", include("apps.vacancy.urls")),
    path("captchaapp/", include("apps.app_captcha.urls")),
    path("user/", include("apps.backendfilter.urls")),
    path("session_verification/", include("apps.session_verification.urls")),
    path("rosetta_example/", include("apps.rosetta_example.urls")),
    path("model_translation/", include("apps.model_translation.urls")),

]
urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
