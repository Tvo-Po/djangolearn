from django.urls import path

from . import views


app_name = 'placegallery'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:slug>/', views.CityView.as_view(), name='city'),
]
