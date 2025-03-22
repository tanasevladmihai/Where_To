from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Event

class EventSerializer(GeoFeatureModelSerializer):
    distance = serializers.SerializerMethodField()  

    class Meta:
        model = Event
        geo_field = 'location'
        fields = ('id', 'name', 'theme', 'distance', 'address', 'start_date', 'end_date', 'description')

    def get_distance(self, obj):
        return obj.distance if hasattr(obj, 'distance') else None