from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class cars(models.Model):
    type = models.CharField(max_length=64)
    car_model = models.CharField(max_length=64)
    car_fuel=models.CharField(max_length=65)
    car_size=models.CharField(max_length=65)
    car_economy=models.CharField(max_length=65)
    purchaser =models.ForeignKey(get_user_model(), on_delete = models.CASCADE)


    def __str__(self):
        return self.type


class engine(models.Model):
    engine_type = models.CharField(max_length=255)
    engine_size= models.IntegerField()
    engine_cylinder=models.IntegerField()

    def str(self):
        return self.engine_type

