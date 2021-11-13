from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
# app_name = 'tour'

urlpatterns = [
    path('', views.home, name='home'),
    path('tour_list/', views.tour_list, name='tour_list'),
    path('cart/', views.cart, name='cart'),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/',views.processOrder, name="process_order"),
   # path('word_diary/', views.wordDiary, name="word_diary"),
    path('travel_diary/', PostListView.as_view(), name="travel_diary"),
    path('travel_diary/post/<int:pk>/', PostDetailView.as_view(), name="travel_diary_detail"),
    path('travel_diary/post/new/', PostCreateView.as_view(), name="travel_diary_create"),
    path('travel_diary/post/<int:pk>/update/', PostUpdateView.as_view(), name="travel_diary_update"),
    path('travel_diary/post/<int:pk>/delete/', PostDeleteView.as_view(), name="travel_diary_delete"),

]
