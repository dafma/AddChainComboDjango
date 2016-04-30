__author__ = 'mrk2'
from rest_framework import serializers
from country.models import Country
from state.models import State
from city.models import City

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerilizer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'