from django.db import models

# Create your models here.

class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    id = models.CharField(max_length=50, primary_key=True)
    working = models.BooleanField(default=False)
    color = models.CharField(max_length=50, default="255, 200, 25")

    def __str__(self):
        return(f'{self.firstName} {self.lastName}')