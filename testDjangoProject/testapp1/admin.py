from django.contrib import admin
from testapp1.models import BookingMachine, MealMachine, OrderMachine

# Register your models here.
admin.site.register(BookingMachine)
admin.site.register(MealMachine)
admin.site.register(OrderMachine)
