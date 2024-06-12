from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.
def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def odjava(request):
    context = {}
    return render(request, 'store/odjava.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items, 'order':order}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    return JsonResponse('Arikal dodat', safe=False)