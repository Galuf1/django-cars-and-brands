from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return Brand.name

class Car(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='cars')
    model = models.CharField(max_length=50)