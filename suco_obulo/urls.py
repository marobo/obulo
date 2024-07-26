from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('nature-and-tourism', views.nature_and_tourism_view, name='nature_and_tourism'),
    path('aldeias', views.aldeias_view, name='aldeias'),
    path('people-and-culture', views.people_and_culture_view, name='people_and_culture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
