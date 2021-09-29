from django.shortcuts import render
from django.views import generic

from .models import City, InterestingPlace


class IndexView(generic.ListView):
    template_name = 'placegallery/index.html'
    context_object_name = 'alphabetical_order_city_list'
    paginate_by = 4

    def get_queryset(self):
        return City.objects.order_by('city_name_ru')[:]


class CityView(generic.DetailView):
    model = City
    template_name = 'placegallery/city.html'


class InterestingPlaceView(generic.DetailView):
    model = InterestingPlace
    template_name = 'placegallery/place.html'
