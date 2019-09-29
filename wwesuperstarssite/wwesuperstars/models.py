import re
import datetime
from django.db import models

# Create your models here.

# Create a class to represent a Superstar which will be child class of the
# Model class which is stored in the models object.

class WWESuperstar(models.Model):
    # Then we will create class variables to represent each column in the database
    # table for this model. Each variable will use a class which is stored in the
    # models module that corresponds with the data type.
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='wwesuperstars/img/' + datetime.datetime.now().strftime("%Y/%m/%d/"))
    age = models.IntegerField()
    # track = models.FileField(upload_to='wwesuperstars/audio/' + datetime.datetime.now().strftime("%Y/%m/%d/"))
    # current_status = models.IntegerField(choices=((1, "Active"), (2, "Part-Timer"), (3, "Retired")))
    retired = models.BooleanField()

    # Filtering/Sanitizing the text inputs
    def clean(self):
        if self.name:
            self.name = self.name.strip()
            self.name = re.sub(r"([^a-zA-Z\-. ]+)", "", self.name)
            self.name = self.name.lower().title()

    #
    def __str__(self):
        return self.name[:50]
