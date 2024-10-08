from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_view, name='about'),
    path('aldeias', views.aldeias_view, name='aldeias'),
    path('nature-tourism', views.nature_and_tourism_view, name='nature_and_tourism'),
    path('people-culture', views.people_and_culture_view, name='people_and_culture'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
