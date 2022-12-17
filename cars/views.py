from django.shortcuts import render

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import carsSerializer, engineSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
from .models import cars, engine
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


class carsListView(ListCreateAPIView):
    queryset = cars.objects.all()
    serializer_class = carsSerializer


class carsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = cars.objects.all()
    serializer_class = carsSerializer
    permission_classes = [IsOwnerOrReadOnly]


class engineListView(ListCreateAPIView):
    queryset = engine.objects.all()
    serializer_class = engineSerializer
    permission_classes = [AllowAny]


class engineDetailView(RetrieveUpdateDestroyAPIView):
    queryset = engine.objects.all()
    serializer_class = engineSerializer
    permission_classes = [AllowAny]
