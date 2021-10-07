from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from . import views


app_name = 'placegallery'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path('^login/$', views.login_system, name='login'),
    re_path('^logout/$', views.logout_system, name='logout'),
    path('profile/', login_required(views.ProfileView.as_view(), login_url='placegallery:register'), name='profile'),
    path('register/', views.registration_system, name='register'),
    path('<slug:slug>/', views.CityView.as_view(), name='city'),
    path('<str:city_name>/<slug:slug>', views.InterestingPlaceView.as_view(), name='place'),
]
