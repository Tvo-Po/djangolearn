from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import City, InterestingPlace


class IndexView(generic.ListView):
    template_name = 'placegallery/index.html'
    context_object_name = 'city_list'
    paginate_by = 26

    def get_queryset(self):
        return City.objects.order_by('region__region_name_ru')[2:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Moscow'] = City.objects.get(slug='Moscow')
        context['SPb'] = City.objects.get(slug='Saint-Petersburg')
        return context


class CityView(generic.DetailView):
    model = City
    template_name = 'placegallery/city.html'


class InterestingPlaceView(generic.DetailView):
    model = InterestingPlace
    template_name = 'placegallery/place.html'


def login_system(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            context = {'authentication_type': 'success',
                       'authentication_text': 'Вы успешно вошли на сайт.'}
            login(request, user)
        else:
            context = {'authentication_type': 'danger',
                       'authentication_text': 'Неверное имя пользователя или пароль.'}
        return render(request, 'placegallery/authentication.html', context=context)


def logout_system(request):
    if request.method == 'GET':
        logout(request)
        context = {'authentication_type': 'success',
                   'authentication_text': 'Вы успешно вышли.'}
        return render(request, 'placegallery/authentication.html', context=context)


def registration_system(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            context = {'authentication_type': 'danger',
                       'authentication_text': 'Введенные пароли не свопадают.'}
        elif User.objects.filter(username=username):
            context = {'authentication_type': 'danger',
                       'authentication_text': 'Пользователь с таким именем уже существует.'}
        else:
            User.objects.create_user(username, password=password1)
            context = {'authentication_type': 'success',
                       'authentication_text': 'Вы успешно зарегестрировались.'}
        return render(request, 'placegallery/authentication.html', context=context)
