from django.db import models

# Create your models here.
class Moto(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=15)
    owner_name = models.CharField(max_length=100)
    service_description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __str__(self):
        return f"{self.brand} {self.model} - {self.license_plate}"