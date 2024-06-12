from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name="store"),
    path('korpa/', views.cart, name='cart'),
    path('checkout/', views.checkout, name="checkout"),
    path('logout/', views.odjava, name='odjava'),
    path('update_item/', views.updateItem, name="update_item"), 
]