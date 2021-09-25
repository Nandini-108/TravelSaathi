from django.conf import settings
from django.db import models
from django.utils import timezone


# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Tour_package(models.Model):
    tour_id = models.IntegerField()
    tour_title = models.CharField(max_length=200)    
    start_dest = models.CharField(max_length=20)
    tour_duration = models.CharField(max_length=10)
    price = models.IntegerField()
    description = models.TextField()
    
    
    def __str__(self):
        return self.tour_title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    tour_title = models.ForeignKey(Tour_package, on_delete=models.CASCADE)
    guests = models.IntegerField(default=1)

    

