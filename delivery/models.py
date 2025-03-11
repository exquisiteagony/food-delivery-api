from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=2)

    objects = models.Manager()

