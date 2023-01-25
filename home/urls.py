from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('album/', views.album, name='album'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]