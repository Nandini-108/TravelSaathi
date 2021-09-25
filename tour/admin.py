from django.contrib import admin

# Register your models here.
from .models import Tour_package, Order

admin.site.register(Tour_package)
admin.site.register(Order)