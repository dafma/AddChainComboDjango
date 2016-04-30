from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from country.models import Country
from state.models import State
from city.models import City
from .serializers import CitySerilizer, CountrySerializer, StateSerializer
import json
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
@csrf_exempt
def get_country(request):
    countryobj = Country.objects.all()
    country_serializer = CountrySerializer(countryobj, many=True)
    response = Response(country_serializer.data)
    return Response(response.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_exempt
def get_state(request, sid):

    #stateobj = State.objects.all()
    stateobj = State.objects.filter(contry=sid)
    #cid =  request.GET.get('cid')

    state_serializer = StateSerializer(stateobj, many=True)
    response = Response(state_serializer.data)

    return Response(response.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@csrf_exempt
def get_city(request, cid):
    #cityobj = City.objects.all()
    cityobj = City.objects.filter(state=cid)
    city_serializer = CitySerilizer(cityobj, many=True)
    response = Response(city_serializer.data)

    return Response(response.data, status=status.HTTP_200_OK)

