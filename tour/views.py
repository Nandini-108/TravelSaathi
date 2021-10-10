from django.shortcuts import render
from .models import Tour_package
# Create your views here.
def tour_list(request):
    context = {
        "tours": Tour_package.objects.all(),
        "tree": "This is me",
        "my_list": [1,2,3]
    }
    return render(request, 'tour/tour_list.html', context)

def home(request):
       context = {}
       return render(request, 'tour/home.html', context)
