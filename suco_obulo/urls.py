from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import re_path
from django.views.static import serve
from django.utils.translation import gettext_lazy as _ # noqa


urlpatterns = [
    path('', views.page, {'template_name': 'index.html'}, name='index'),
    path(
        'about',
        views.page,
        {'template_name': 'suco_obulo/about.html'},
        name='about',
    ),
    path(
        'aldeias',
        views.page,
        {
            'template_name': 'suco_obulo/section_page.html',
            'page_name': _('Aldeias'),
        },
        name='aldeias',
    ),
    path(
        'nature-tourism',
        views.page,
        {
            'template_name': 'suco_obulo/section_page.html',
            'page_name': _('Nature & Tourism'),
        },
        name='nature_and_tourism',
    ),
    path(
        'people-culture',
        views.page,
        {
            'template_name': 'suco_obulo/section_page.html',
            'page_name': _('People & Culture'),
        },
        name='people_and_culture',
    ),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
