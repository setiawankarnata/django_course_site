from django.db import models
from django.utils.timezone import datetime


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField(default="organizer@mail.com")
    meetup_date = models.DateField(default=datetime.today())
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location2meetup', default=None)
    participants = models.ManyToManyField(Participant, related_name="participant2meetup", blank=True)

    def __str__(self):
        return f"{self.title} - {self.slug}"
