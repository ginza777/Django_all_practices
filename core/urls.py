# imports
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from .schema import swagger_urlpatterns

# model translation
from django.urls.exceptions import Resolver404
from django.utils import translation
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.conf.urls.i18n import i18n_patterns


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("authentication/", include("apps.authentication.urls")),
    path("befit/", include("apps.befit.urls")),
    path("vacancy/", include("apps.vacancy.urls")),
    path("app_captcha/", include("apps.app_captcha.urls")),
    path("backendfilter/", include("apps.backendfilter.urls")),
    path("session_verification/", include("apps.session_verification.urls")),
    path("rosetta_example/", include("apps.rosetta_example.urls")),
    path("model_translation/", include("apps.model_translation.urls")),
    path("djangosignals/", include("apps.djangosignals.urls")),

]
# swagger url settings
urlpatterns += swagger_urlpatterns

# media url settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# model translation url settings
urlpatterns = [
    *i18n_patterns(*urlpatterns),
    path("set_language/<str:language>", set_language, name="set-language"),
]
# rosetta settings

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
