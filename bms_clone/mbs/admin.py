from django.contrib import admin
from .models import City, Theatre, Screen, Seats, Slot, Movie, ScreenSlotMovieMapping

admin.site.register(City)
admin.site.register(Theatre)
admin.site.register(Screen)
admin.site.register(Seats)
admin.site.register(Slot)
admin.site.register(Movie)
admin.site.register(ScreenSlotMovieMapping)
