from django.contrib.gis.geos import Point
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from GeoApp.models import Building
from .views import BuildingViewSet

class BuildingFilterTestCase(TestCase):
    def setUp(self):
        self.building1 = Building.objects.create(name="Building 1", geom=Point(39.7137112, 47.2313))
        self.building2 = Building.objects.create(name="Building 2", geom=Point(40.0, 47.0))

    def test_building_filter(self):
        factory = APIRequestFactory()
        view = BuildingViewSet.as_view({'get': 'list'})
        url = '/buildings/?latitude=47.2313&longitude=39.7137112&distance=100'

        request = factory.get(url)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Building 1")