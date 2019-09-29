import re
import datetime
from django.db import models
from wwesuperstars.models import WWESuperstar

class Movie(models.Model):
    title = models.CharField(max_length=255)
    wwesuperstars = models.ForeignKey(WWESuperstar, on_delete=models.CASCADE, blank=True, related_name='movie')

    def clean(self):
        if self.title:
            self.title = self.title.strip()
            self.title = re.sub(r"([^a-zA-Z\-. ]+)", "", self.title)
            self.title = self.title.lower().title()

    def __str__(self):
        return self.title[:50]

class Poster(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, primary_key=True, related_name='poster')
    role = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='movies/posters/' + datetime.datetime.now().strftime("%Y/%m/%d/"))

    def clean(self):
        if self.role:
            self.role = self.role.strip()
            self.role = re.sub(r"([^a-zA-Z\-. ]+)", "", self.role)
            self.role = self.role.lower().title()

    def __str__(self):
        return self.role[:50]

    def __str__(self):
        return self.image
