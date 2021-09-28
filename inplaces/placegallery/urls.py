from django.urls import path

from . import views


app_name = 'placegallery'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.CityView.as_view(), name='city'),
    path('<str:city_name>/<slug:slug>', views.InterestingPlaceView.as_view(), name='place'),
]
