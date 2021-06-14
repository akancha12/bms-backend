from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class City(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return str(self.name)


class Theatre(models.Model):
    name = models.CharField(max_length=50, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.name)


class Screen(models.Model):
    name = models.CharField(max_length=50, null=False)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Seats(models.Model):
    row = models.CharField(max_length=1, null=False)
    index = models.IntegerField(null=False)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)

    def __str__(self):
        return "seat is %s-%s % (self.row, self.index)"


class Slot(models.Model):
    start_timestamp = models.DateTimeField(default=timezone.now)
    end_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "slot is from %s-%s" % (self.start_timestamp, self.end_timestamp)


class Movie(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.name)

class ScreenSlotMovieMapping(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
