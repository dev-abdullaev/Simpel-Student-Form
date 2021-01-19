from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    stduent_ID = models.CharField(max_length=250)
    course = models.CharField(max_length=250)

    def __str__(self):
        return self.name + ' | ' + self.stduent_ID
