from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.IntegerField()
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    department = models.CharField(max_length=100)
    salary = models.FloatField()
    experience = models.IntegerField()

    def __str__(self):
        return self.name