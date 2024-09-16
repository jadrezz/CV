from django.contrib.gis.geos import Polygon, Point
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Building


class BuildingSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Building
        geo_field = 'geom'
        fields = ('id', 'address', 'geom')

    def validate_geom(self, value):
        if not isinstance(value, Point):
            raise serializers.ValidationError("Поле geom должно быть объектом Point")

        if not value.valid:
            raise serializers.ValidationError("Поле geom заполнено некорректно")

        return value
