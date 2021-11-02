from django.shortcuts import render
from .models import StartDest, Tour_package, Order
from .models import *
from django.http import JsonResponse
import json
import datetime
# Create your views here.
def tour_list(request):
    context = {
        "tours": Tour_package.objects.all(),
        "starts": StartDest.objects.all(),
    }
    return render(request, 'tour/tour_list.html', context)

def home(request):
       context = {}
       return render(request, 'tour/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer= request.user
        order, created= Order.objects.get_or_create(customer=customer, complete= False)
        items= order.orderitem_set.all()
        
    else:
        items=[] 
        order = {'get_cart_total': 0} 
        
    
    context = {'items': items, 'order': order}
    return render(request, 'tour/cart.html', context)  


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user
    product = Tour_package.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, tour=product)
	
    if action == 'add':
    	orderItem.guests = (orderItem.guests + 1)
    elif action == 'remove':
    	orderItem.guests = (orderItem.guests - 1)

    orderItem.save()

    if orderItem.guests <= 0:
    	orderItem.delete()
    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order.transaction_id = transaction_id

        order.complete = True
        order.save()
    return JsonResponse('Processed',safe=False)