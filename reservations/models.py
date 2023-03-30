from django.db import models


class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
