from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import City, Theatre, Screen, Slot, Movie, Seats, ScreenSlotMovieMapping
from .serializers import CitySerializer, TheatreSerializer, ListTheatreSerializer, SeatSerializer, SlotSerializer, \
    MovieSerializer, ScreenSlotMovieMappingSerializer, ScreenSerializer, ListScreenSerializer, ListSeatSerializer, \
    ListScreenSlotMovieMappingSerializer
from .permissions import IsAdminOrReadOnly


class CityView(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = City.objects.all()

    @action(methods=['GET'], detail=True)
    def theatre(self, request, *args, **kwargs):
        city_id = self.kwargs['pk']
        theatre_list = Theatre.objects.filter(city=city_id)
        serializer = ListTheatreSerializer(theatre_list, many=True)
        return Response(serializer.data)


class TheatreView(viewsets.ModelViewSet):
    serializer_class = TheatreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Theatre.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return TheatreSerializer
        return ListTheatreSerializer


class ScreenView(viewsets.ModelViewSet):
    serializer_class = ScreenSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Screen.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ScreenSerializer
        return ListScreenSerializer


class SeatView(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Seats.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return SeatSerializer
        return ListSeatSerializer


class SlotView(viewsets.ModelViewSet):
    serializer_class = SlotSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Slot.objects.all()


class MovieView(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Movie.objects.all()


class ScreenSlotMovieMappingView(viewsets.ModelViewSet):
    serializer_class = ScreenSlotMovieMappingSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = ScreenSlotMovieMapping.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return ScreenSlotMovieMappingSerializer
        return ListScreenSlotMovieMappingSerializer
