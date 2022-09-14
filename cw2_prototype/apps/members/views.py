# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from .models import stock
from django.urls import reverse

def index(request):
    st = stock.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'stock': st
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse(template.render())

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
    update = stock(item_name=name, item_type=item_type, cat=cat, brand_name=brand, qty=qty, price=price)
    update.save()
    return HttpResponseRedirect(reverse('index'))

def search_record(request):
    search_input_id = request.GET['sr_id']
    search_input_name = request.GET['sr_na']
    search_input_type = request.GET['sr_ty']
    search_input_cat = request.GET['sr_cat']
    search_input_brand = request.GET['sr_br']
    search_result = stock.objects.filter(item_name = search_input_name.capitalize()).values()
    
    template = loader.get_template('search_result.html')
    context = {
        'stock' : search_result
    }
    return HttpResponse(template.render(context, request))