from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LocaionsSerializer
from .models import Locaions
from rest_framework.response import Response

from geopy.geocoders import Nominatim
from datetime import datetime



class LocaionsViewSet(APIView):


    def get(self, request, format=None):
        # 
        if request.GET.__len__() > 0:
                get_data = request.GET
        else:
            get_data = request.query_params
        
        geolocator = Nominatim(user_agent="nominatim")
        # location = geolocator.reverse(get_data['latitude'], get_data['longitude'])
        # import pdb; pdb.set_trace()
        location = geolocator.reverse("9.999, 10.545")
        ins_Locaion = Locaions(location_name = location.address,time = datetime.now())
        locations = Locaions.objects.all()
        serializer = LocaionsSerializer(locations, many=True)
        return Response(serializer.data)
