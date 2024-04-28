from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.email)

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_number = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    vehicle_color = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0}, {1}'.format(self.vehicle_number, self.vehicle_type)

class Violation(models.Model):
    id = models.AutoField(primary_key=True)
    licence = models.CharField(max_length=100)
    date_incidence= models.DateTimeField(auto_now_add=True)
    official_comment = models.TextField()
    email = models.EmailField(null=True)

    def __str__(self):
        return '{0}, {1}'.format(self.licence, self.email)