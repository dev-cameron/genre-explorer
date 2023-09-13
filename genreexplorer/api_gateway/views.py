from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests

# Create your views here.
@api_view(['GET']) #will accept GET requests to endpoint: localhost:8000/api-gateway/pokemon-id
@permission_classes([AllowAny]) #allow any user to access this endpoint
def pokemon_id_view(request):
    api_url = "https://pokeapi.co/api/v2/pokemon/1/"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json() #parse the json response into a python dictionary

        return Response(data) #return data as a json response
  
    else:
        return Response({"message": "Unable to get data from API"}, status=response.status_code)