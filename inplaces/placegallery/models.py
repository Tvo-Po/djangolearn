import os

from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    region_name_ru = models.CharField(max_length=50, verbose_name='russian name')
    population = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.region_name_ru

    def save(self, *args, **kwargs):
        if not self.population:
            self.population = None
        if not self.area:
            self.area = None
        super(Region, self).save(*args, **kwargs)


class City(models.Model):
    slug = models.CharField(max_length=50, verbose_name='english name for URL')
    city_name_ru = models.CharField(max_length=50, verbose_name='russian name')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    population = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.city_name_ru

    def get_place_queryset(self):
        return self.places.all()

    def save(self, *args, **kwargs):
        if not self.population:
            self.population = None
        if not self.area:
            self.area = None
        super(City, self).save(*args, **kwargs)


class InterestingPlace(models.Model):
    slug = models.CharField(max_length=200, verbose_name='english name for URL')
    interesting_place_name_ru = models.CharField(max_length=200, verbose_name='russian name')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='places')
    street_name = models.CharField(max_length=100, blank=True)
    house_number = models.CharField(max_length=10, blank=True)
    cord_x = models.FloatField(verbose_name='X coordinate')
    cord_y = models.FloatField(verbose_name='Y coordinate')
    description = models.TextField(blank=True)

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


def create_image_path_for_user(instance, filename):
    return os.path.join(
        'placegallery',
        'static',
        'user_profile_image',
        instance.user.username,
        filename
    )


class PlaceImage(models.Model):
    image = models.ImageField(upload_to=create_image_path)
    interesting_place = models.ForeignKey(InterestingPlace, on_delete=models.CASCADE)

    def get_relative_path(self):
        path = self.image.path
        return path[path.find('place_images'):]


class UserProfile(models.Model):
    img_profile = models.ImageField(upload_to=create_image_path_for_user)
    user = models.OneToOneField(User, models.CASCADE)

    def get_relative_path(self):
        path = self.img_profile.path
        return path[path.find('user_profile_image'):]
