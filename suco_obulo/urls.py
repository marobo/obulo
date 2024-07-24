from django.urls import path
from . import views


urlpatterns = [
    path('aldeias', views.list_aldeia_view, name='aldeia_list'),
    path('aldeia-detail', views.detail_aldeia_view, name='aldeia_detail'),
]
