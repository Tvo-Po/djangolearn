from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Region, City, InterestingPlace, PlaceImage, UserProfile


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_name_ru',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    # inlines = [RegionInline]
    list_display = ('city_name_ru', 'population')
    fieldsets = (
        (None,
         {
             'fields': ('region', ('slug', 'city_name_ru'),)
         }),
        ('City Info',
         {
             'fields': ('population', 'area')
         })
    )


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage


@admin.register(InterestingPlace)
class InterestingPlaceAdmin(admin.ModelAdmin):
    list_display = ('interesting_place_name_ru',)
    fieldsets = (
        (None,
         {
             'fields': (('slug', 'interesting_place_name_ru'), 'description')
         }),
        ('Place Address',
         {
             'fields': ('city', 'street_name', 'house_number')
         }),
        ('Map',
         {
             'fields': ('cord_x', 'cord_y')
         })
    )
    inlines = [PlaceImageInline]


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
