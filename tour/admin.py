from django.contrib import admin

# Register your models here.
from .models import Tour_package, Order, StartDest

admin.site.register(StartDest)
admin.site.register(Tour_package)
admin.site.register(Order)