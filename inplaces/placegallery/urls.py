from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView),
    path('<str:city_name>/', views.IndexView)
]
