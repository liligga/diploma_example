from django.db import models
from django.contrib.auth.models import User


class House(models.Model):
    title = models.CharField(max_length = 150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self. title


class HouseDetail(models.Model):
    number_of_bedrooms = models.IntegerField()
    floor_number = models.IntegerField()
    
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    

    
class HouseImage(models.Model):
    file = models.ImageField(upload_to='houses')
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    
    