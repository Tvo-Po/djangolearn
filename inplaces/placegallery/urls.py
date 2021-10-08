from django.urls import path, re_path
from django.contrib.auth.decorators import login_required

from . import views


app_name = 'placegallery'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path('^login/$', views.login_system, name='login'),
    re_path('^logout/$', views.logout_system, name='logout'),
    path('register/', views.registration_system, name='register'),
    path('profile/', login_required(views.ProfileView.as_view(), login_url='placegallery:register'), name='profile'),
    path('comment/', login_required(views.CommentView.as_view(), login_url='placegallery:register'), name='comment'),
    path('add_place', login_required(views.NewPlaceView.as_view()), name='add_place'),
    path('<slug:slug>/', views.CityView.as_view(), name='city'),
    path('<str:city_name>/<slug:slug>', views.InterestingPlaceView.as_view(), name='place'),
]
