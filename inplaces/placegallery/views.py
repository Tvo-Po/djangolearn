from django.shortcuts import render
from django.views import generic

from .models import City


class IndexView(generic.ListView):
    template_name = 'placegallery/index.html'
    context_object_name = 'alphabetical_order_city_list'

    def get_queryset(self):
        return City.objects.all().order_by('city_name')[:5]


class CityView(generic.DetailView):
    pass
