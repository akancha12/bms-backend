from rest_framework import serializers
from django.contrib.auth import get_user_model
import re
from rest_framework.exceptions import ValidationError
from .models import City, Theatre, Screen, Seats, Slot, Movie, ScreenSlotMovieMapping

User = get_user_model()


class CitySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
    )

    class Meta:
        model = City
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class TheatreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
    )
    # city = CitySerializer()
    address = serializers.CharField(
        required=True,
    )

    class Meta:
        model = Theatre
        fields = '__all__'


class ScreenSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
    )

    class Meta:
        model = Screen
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    row = serializers.CharField(
        required=True,
    )
    index = serializers.IntegerField(
        required=True,
    )

    class Meta:
        model = Seats
        fields = '__all__'


class SlotSerializer(serializers.ModelSerializer):
    start_timestamp = serializers.DateTimeField(
        required=True,
    )
    end_timestamp = serializers.DateTimeField(
        required=True
    )

    class Meta:
        model = Slot
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
    )

    class Meta:
        model = Movie
        fields = '__all__'


class ScreenSlotMovieMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreenSlotMovieMapping
        fields = '__all__'
