from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import City, Theatre, Screen, Slot, Movie, Seats, ScreenSlotMovieMapping
from .serializers import CitySerializer, TheatreSerializer, ScreenSerializer, SeatSerializer, SlotSerializer, MovieSerializer, ScreenSlotMovieMappingSerializer


class CityView(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = City.objects.all()


class TheatreView(viewsets.ModelViewSet):
    serializer_class = TheatreSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = Theatre.objects.all()


class ScreenView(viewsets.ModelViewSet):
    serializer_class = ScreenSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = Screen.objects.all()


class SeatView(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = Seats.objects.all()


class SlotView(viewsets.ModelViewSet):
    serializer_class = SlotSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = Slot.objects.all()


class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = Movie.objects.all()


class ScreenSlotMovieMappingView(viewsets.ModelViewSet):
    serializer_class = ScreenSlotMovieMappingSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = ScreenSlotMovieMapping.objects.all()
