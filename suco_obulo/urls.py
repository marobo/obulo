from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('aldeias', views.list_aldeia_view, name='aldeia_list'),
    path('aldeia-detail', views.detail_aldeia_view, name='aldeia_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
