from django.urls import include, path
from portcoreapi import views


urlpatterns = [
    path('', views.category),
    path('about/', views.category),
    path('education/', views.category),
    path('exp/', views.category),
    path('skills/', views.category),
    path('cert/', views.category),
    path('lang/', views.category),
    path('contact/', views.category),
    path('add_category/', views.category),
    path('add_exp/', views.category),
    path('request_viev/', views.category),
]