import os

from django.db import models


class City(models.Model):
    slug = models.CharField(max_length=50)
    city_name_ru = models.CharField(max_length=50)
    population = models.IntegerField()
    area = models.FloatField()

    def __str__(self):
        return self.city_name_ru

    def get_place_queryset(self):
        return self.places.all()


class InterestingPlace(models.Model):
    slug = models.CharField(max_length=200)
    interesting_place_name_ru = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')
    street_name = models.CharField(max_length=100, blank=True)
    house_number = models.CharField(max_length=10, blank=True)
    cord_x = models.FloatField()
    cord_y = models.FloatField()

    def __str__(self):
        return self.interesting_place_name_ru


def create_image_path(instance, filename):
    return os.path.join(
        'placegallery',
        'static',
        'place_images',
        instance.interesting_place.city.slug,
        instance.interesting_place.slug,
        filename
    )


class PlaceImage(models.Model):
    image = models.ImageField(upload_to=create_image_path)
    interesting_place = models.ForeignKey(InterestingPlace, on_delete=models.CASCADE)

    def get_relative_path(self):
        path = self.image.path
        return path[path.find('place_images'):]
