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
    item = list(stock.objects.values_list('id', flat=True))
    id = 1
    for _ in range(item[-1]+1):
        if id not in item:
            itemID = id
            id = 1
            break
        id += 1
    name = request.POST['name'].upper()
    cat = request.POST['cat'].upper()
    brand = request.POST['brand'].upper()
    qty = request.POST['qty'].upper()
    price = request.POST['price'].upper()
    update = stock(id=itemID,item_name=name, cat=cat, brand_name=brand, qty=qty, price=price)
    update.save()
    return back_main()
    # return HttpResponseRedirect(reverse('index'))

def search_record(request):
    search_input_id = request.GET['sr_id']
    search_input_name = request.GET['sr_na']
    search_input_cat = request.GET['sr_cat']
    search_input_brand = request.GET['sr_br']
    search_result = stock.objects.filter(item_name = search_input_name.upper()).values()
    
    template = loader.get_template('search_result.html')
    context = {
        'stock' : search_result
    }
    return HttpResponse(template.render(context, request))

def edit(request, id):
    item = stock.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'stock': item,
    }
    return HttpResponse(template.render(context, request))

def edit_record(request, id):
    name = request.POST['name'].upper()
    cat = request.POST['cat'].upper()
    brand = request.POST['brand'].upper()
    qty = request.POST['qty'].upper()
    price = request.POST['price'].upper()
    item = stock.objects.get(id=id)
    item.item_name = name
    item.cat = cat
    item.brand_name = brand
    item.qty = qty
    item.price = price
    item.save()
    return back_main()

def remove_record(request, id):
    item = stock.objects.get(id = id)
    item.delete()
    return back_main()

def back_main():
    return HttpResponseRedirect(reverse('index'))