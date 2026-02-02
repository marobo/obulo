"""
URL configuration for obulo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include, re_path

from obulo.serve_files import serve_static, serve_media

# Static and media MUST be at the top so /static/ and /media/ are matched
# before i18n_patterns(path('', include(...))) catches everything.
if settings.DEBUG:
    urlpatterns = (
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
else:
    urlpatterns = [
        re_path(r"^static/(?P<path>.*)$", serve_static),
        re_path(r"^media/(?P<path>.*)$", serve_media),
    ]

urlpatterns = list(urlpatterns) + list(
    i18n_patterns(
        path("admin/", admin.site.urls),
        path("i18n/", include("django.conf.urls.i18n")),
        path("summernote/", include("django_summernote.urls")),
        path("", include("suco_obulo.urls")),
        prefix_default_language=False,
    )
)
if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [
        path("rosetta/", include("rosetta.urls")),
    ]
