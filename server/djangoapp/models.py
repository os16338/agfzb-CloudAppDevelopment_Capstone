from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    type_ch = models.CharField(max_length=10, choices=(('BMW', 'BMW',), ('Benz', 'Benz'), ('Swift', 'Swift')))
    id = models.IntegerField(null=False,primary_key=True)
    year = models.DateField()

    def __str__(self):
        return self.name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
