from django.shortcuts import render
from .models import StartDest, Tour_package, Order, TravelDiary
from .models import *
from django.http import JsonResponse
import json
import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


def wordDiary(request):
    return render(request, 'tour/wordDiary.html')

def travelDiary(request):
    return render(request, 'tour/travelDiary.html', {"posts": TravelDiary.objects.all()})

class PostListView(ListView):
    model = TravelDiary
    template_name = 'tour/travelDiary.html'
    context_object_name = 'posts'
    #ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = TravelDiary

class PostCreateView(LoginRequiredMixin, CreateView):
    model = TravelDiary
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TravelDiary
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TravelDiary
    success_url = '/travel_diary'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False