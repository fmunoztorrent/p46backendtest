from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('single_digits_ep', views.single_digits_ep, name='single_digits_ep'),
]