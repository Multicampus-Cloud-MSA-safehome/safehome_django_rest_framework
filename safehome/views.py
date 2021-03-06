from django.shortcuts import render

from django.shortcuts import render
from rest_framework import generics
from django.db.models import Subquery

from .models import Region, Alcohol, Children, Crime, Fire_damage, Flood, House, Population,\
   Total, Total_rate, Draw_data
from .serializers import RegionSerializer, AlcoholSerializer, ChildrenSerializer, CrimeSerializer, FireDamageSerializer,\
   FloodSerializer, HouseSerializer, PopulationSerializer, TotalSerializer, TotalRateSerializer, DrawdataSerializer

# Region
class ListRegion(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class DetailRegion(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

# Alcohol
class ListAlcohol(generics.ListCreateAPIView):
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer

class DetailAlcohol(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer

# children
class ListChildren(generics.ListCreateAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

class DetailChildren(generics.RetrieveUpdateDestroyAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

# crime
class ListCrime(generics.ListCreateAPIView):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer

class DetailCrime(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crime.objects.all()
    serializer_class = CrimeSerializer

# fire_damage
class ListFire(generics.ListCreateAPIView):
    queryset = Fire_damage.objects.all()
    serializer_class = FireDamageSerializer

class DetailFire(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fire_damage.objects.all()
    serializer_class = FireDamageSerializer

# flood
class ListFlood(generics.ListCreateAPIView):
    queryset = Flood.objects.all()
    serializer_class = FloodSerializer

class DetailFlood(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flood.objects.all()
    serializer_class = FloodSerializer

# house
class ListHouse(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class DetailHouse(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

# population
class ListPopulation(generics.ListCreateAPIView):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer

class DetailPopulation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer

# total
class ListTotal(generics.ListCreateAPIView):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer

class DetailTotal(generics.RetrieveUpdateDestroyAPIView):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer

# total_rate
class ListTotalRate(generics.ListCreateAPIView):
    queryset = Total_rate.objects.all()
    serializer_class = TotalRateSerializer

class DetailTotalRate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Total_rate.objects.all()
    serializer_class = TotalRateSerializer

# svgd
class ListDrawdata(generics.ListCreateAPIView):
    queryset = Draw_data.objects.all()
    serializer_class = DrawdataSerializer

class DetailDrawdata(generics.RetrieveUpdateDestroyAPIView):
    queryset = Draw_data.objects.all()
    serializer_class = DrawdataSerializer
