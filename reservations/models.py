from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Available"), (1, "Reserved"))


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    # Added a validator to limit the capacity to 5
    capacity = models.IntegerField(validators=[MaxValueValidator(5)])
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"Table {self.table_number}"


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer} - {self.date} {self.time}"


@receiver(post_migrate)
def create_tables(sender, **kwargs):
    for i in range(1, 6):  # Created 5 tables
        Table.objects.get_or_create(table_number=i, capacity=5)
