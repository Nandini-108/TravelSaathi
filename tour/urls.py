from django.urls import path
from . import views

# app_name = 'tour'

urlpatterns = [
    path('', views.home, name='home'),
    path('tour_list/', views.tour_list, name='tour_list'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/',views.processOrder, name="process_order"),
    path('word_diary/', views.wordDiary, name="word_diary"),
    path('travel_diary/', views.travelDiary, name="travel_diary"),
]