import os

from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=50)
    population = models.IntegerField()
    area = models.FloatField()

    def __str__(self):
        return self.city_name


class InterestingPlace(models.Model):
    interesting_place_name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10, blank=True)
    cord_x = models.FloatField()
    cord_y = models.FloatField()

    def __str__(self):
        return self.interesting_place_name


def create_image_path(instance, filename):
    return os.path.join(
        instance.interesting_place.city.city_name,
        instance.interesting_place.interesting_place_name,
        filename
    )


class PlaceImage(models.Model):
    image = models.ImageField(upload_to=create_image_path)
    interesting_place = models.ForeignKey(InterestingPlace, on_delete=models.CASCADE)
