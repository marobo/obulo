from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import re_path
from django.views.static import serve


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
            'page_title': 'Aldeias',
            'page_name': 'Aldeias',
            'page_name_tetum': 'Aldeia sira',
        },
        name='aldeias',
    ),
    path(
        'nature-tourism',
        views.page,
        {
            'template_name': 'suco_obulo/section_page.html',
            'page_title': 'Nature & Tourism',
            'page_name': 'Nature & Tourism',
            'page_name_tetum': 'Natureza & Turizmu',
        },
        name='nature_and_tourism',
    ),
    path(
        'people-culture',
        views.page,
        {
            'template_name': 'suco_obulo/section_page.html',
            'page_title': 'People & Culture',
            'page_name': 'People & Culture',
            'page_name_tetum': 'Ema & Kultura',
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
