from django.urls import re_path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import CityView, TheatreView, ScreenView, SlotView, SeatView, MovieView, ScreenSlotMovieMappingView

router = DefaultRouter()
router.register(r'city', CityView)
router.register(r'theatre', TheatreView)
router.register(r'screen', ScreenView)
router.register(r'slot', SlotView)
router.register(r'seat', SeatView)
router.register(r'movie', MovieView)
router.register(r'movie', MovieView)
router.register(r'sms', ScreenSlotMovieMappingView)


urlpatterns = [
    re_path(r'', include(router.urls)),
]
