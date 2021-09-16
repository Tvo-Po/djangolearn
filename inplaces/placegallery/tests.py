from django.test import TestCase

from .models import City, InterestingPlace, PlaceImage, create_image_path


class PlaceImageModelTests(TestCase):
    def test_path_name_for_image(self):
        """
        Path name should be like city_name/place_name/filename,
        where filename is image with location of said place and
        city.
        """
        origin_picture_location = 'C:/Users/Home/Downloads/R2.png'
        city_names = ('Moscow', 'Saint-Petersburg', 'Paris', 'London', 'New York')
        place_names = ('Stonehenge', 'Red Square', 'Peterhoff', 'Louvre', 'Central Park')
        image_names = ('view_1.png', 'view_2.png', 'view_3.png', 'view_4.png', 'view_5.png')
        for i in range(5):
            city = city_names[i]
            place = place_names[i]
            image = image_names[i]
            test_city = City(city_name=city)
            test_place = InterestingPlace(interesting_place_name=place, city=test_city)
            test_image = PlaceImage(image=origin_picture_location, interesting_place=test_place)
            self.assertEqual(create_image_path(test_image, image), city + '\\' + place + '\\' + image)
