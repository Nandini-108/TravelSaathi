from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name=models.CharField(max_length=2000, null=True)
#     email=models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

class StartDest(models.Model):
    start_dest=models.CharField(max_length=20)

    def __str__(self):
        return self.start_dest

class Tour_package(models.Model):
    tour_id = models.IntegerField()
    tour_title = models.CharField(max_length=200)    
    start_dest = models.ForeignKey(StartDest, on_delete=models.CASCADE)
    tour_duration = models.CharField(max_length=10)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)    
    
    def __str__(self):
        return self.tour_title
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url                

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    complete=models.BooleanField(default=False)  
    transaction_id=models.CharField(max_length=100,null=True) 

    def __str__(self):
        return str(self.id) 
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.guests for item in orderitems])
        return total



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    tour = models.ForeignKey(Tour_package, on_delete=models.SET_NULL, null=True)
    guests = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total=self.tour.price * self.guests
        return total



class WordsDiary(models.Model):
    #word_no = models.IntegerField(primary_key = True)
    #Not needed as django automatically adds a field to hold primary key
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    word = models.CharField(max_length = 100)
    meaning = models.TextField()
    language = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)

    def __str__(self):
        return self.word


class TravelDiary(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    visibleToCommunity = models.BooleanField(default = True)
    state = models.CharField(max_length = 50)

    def __str__(self):
        return self.title