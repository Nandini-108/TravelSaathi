from django.shortcuts import render
from .models import StartDest, Tour_package
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
    context = {}
    return render(request, 'tour/cart.html', context)       
