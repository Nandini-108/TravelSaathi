from django.contrib import admin

# Register your models here.
from .models import Tour_package, Order, StartDest, OrderItem, TravelDiary

admin.site.register(StartDest)
admin.site.register(Tour_package)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(Customer)
admin.site.register(TravelDiary)
