from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import City, InterestingPlace, UserProfile, Comment
from .forms import UserBaseSettings, UserAdditionalSettings, UserComment


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

    def get_context_data(self, **kwargs):
        context = super(InterestingPlaceView, self).get_context_data(**kwargs)
        place = context['interestingplace']
        context['comments'] = Comment.objects.filter(place=place).order_by('date')
        context['comment_form'] = UserComment()
        return context


class CommentView(generic.View):

    def post(self, request):
        form = UserComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            place = InterestingPlace.objects.get(slug=request.POST['place'])
            comment.place = place
            comment.save()
            return redirect('placegallery:place', city_name=place.city.slug, slug=place.slug)


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
    if request.method == 'GET':
        context = {'authentication_type': 'danger',
                   'authentication_text': 'Необходимо зарегестрироваться, чтобы зайти на эту страницу.'}
        return render(request, 'placegallery/authentication.html', context=context)
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


class ProfileView(generic.View):
    base_form = UserBaseSettings()
    additional_form = UserAdditionalSettings()

    def _inner_context_make(self, request, username=None):
        if not username:
            user = User.objects.get(username=request.user.username)
        else:
            user = User.objects.get(username=username)
        context = {'base_form': self.base_form, 'additional_form': self.additional_form, 'user': user}
        try:
            user_image = user.userprofile.get_relative_path()
            context['user_pic'] = user_image
        except UserProfile.DoesNotExist:
            user_image = 'user_profile_image/default.png'
            context['user_pic'] = user_image
        finally:
            return context

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        context = self._inner_context_make(request)
        return render(request, 'placegallery/user_profile.html', context)

    def post(self, request):
        if request.POST.get('username'):
            user = User.objects.get(username=request.user.username)
            user.username = request.POST['username']
            user.save()
            context = self._inner_context_make(request, username=request.POST['username'])
            return render(request, 'placegallery/user_profile.html', context)
        if request.POST.get('password'):
            user = User.objects.get(username=request.user.username)
            user.set_password(request.POST.get('password'))
            user.save()
            context = self._inner_context_make(request)
            return render(request, 'placegallery/user_profile.html', context)
        user = User.objects.get(username=request.user.username)
        form = UserAdditionalSettings(request.POST, request.FILES)
        if form.is_valid():
            try:
                current_profile = user.userprofile
                current_profile.delete()
            except UserProfile.DoesNotExist:
                pass
            finally:
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
        context = self._inner_context_make(request)
        return render(request, 'placegallery/user_profile.html', context)
