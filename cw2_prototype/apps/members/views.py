from http.client import HTTPResponse
from re import template
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from .models import stock_item
from django.urls import reverse

def index(request):
    stock = stock_item.objects.all().values()
    template = loader.get_template('index.html')
    context = {'stock': stock}
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    name = request.POST['name']
    item_type = request.POST['type']
    cat = request.POST['cat']
    brand = request.POST['brand']
    qty = request.POST['qty']
    price = request.POST['price']
    update = stock_item(item_name=name, item_type=item_type, cat=cat, brand_name=brand, qty=qty, price=price)
    return HttpResponseRedirect(reverse('index'))