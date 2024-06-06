from django.db import models


# Create your models here.

class BookingMachine(models.Model):
    phone_number = models.CharField(max_length=25, blank=True)
    surname = models.CharField(max_length=20, blank=True)
    isfree = models.BooleanField(default=True, blank=False)

    def save(self, *args, **kwargs):
        self.isfree = False
        super(BookingMachine, self).save(*args, **kwargs)

    def __str__(self):
        return self.surname


class MealMachine(models.Model):
    name = models.CharField(max_length=40, blank=True)
    price = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    preview_picture = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class OrderMachine(models.Model):
    cost = models.IntegerField(blank=True)
    delivery_address = models.CharField(max_length=100, blank=True)
    content = models.ManyToManyField(MealMachine, related_name='orders', blank=True, null=True)



