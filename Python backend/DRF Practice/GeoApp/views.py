from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .models import Building
from .serializers import BuildingSerializer


import math

def distance_to_decimal_degrees(distance, latitude):
    lat_radians = latitude * (math.pi / 180)
    return distance.m / (111_319.5 * math.cos(lat_radians))


# ?latitude=47.2313&longitude=39.7137112&distance=100 test mark
class BuildingFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        distance = request.query_params.get('distance')

        if latitude and longitude and distance:
            point = Point(float(longitude), float(latitude), srid=4326)
            queryset = queryset.filter(geom__dwithin=(point, distance_to_decimal_degrees(Distance(m=distance), float(longitude))))

        return queryset

class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = [BuildingFilter]



