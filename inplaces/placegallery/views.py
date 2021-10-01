from django.shortcuts import render
from django.views import generic

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
