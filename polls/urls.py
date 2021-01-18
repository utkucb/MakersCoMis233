from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photo_1', views.photo_1, name='photo_1'),
    path('photo_2', views.photo_2, name='photo_2'),
    path('contact', views.contact, name='contact'),
    path('choise', views.choise, name='choise'),
]
