from glob import glob
from django.shortcuts import render
from django.http import HttpResponse
from .models import customer,menu,order
# Create your views here.

def name(request, hello):
    data = {
        'hello':hello
    }
    return render(request, 'index.html', data)
    

def customer_all(request):
    a = customer.objects.all()
    if request.method == 'POST':
        username = request.POST['name']
        usercontact = request.POST['contact']
        useraddress = request.POST['address']

        b = customer(customer_name = username, contact = usercontact, address = useraddress)
        b.save()

        return render(request, "customer.html", {'customers': a})
    else:
        return render(request, "customer.html", {'customers': a})

def menu_all(request):
    men = menu.objects.all()
    if request.method == 'POST':
        pname = request.POST['pname']
        global price
        price = request.POST['price']
        global quantity
        quantity = request.POST['quantity']
        type = request.POST['type']
        data = menu(pizza_name=pname,is_veg=type,quantity=quantity,price=price)
        data.save()
        return render(request,'menu.html',{'menu':men})
    else:
        return render(request,'menu.html',{'menu':men})


def order_all(request):
    ord = order.objects.all()
    total_amount = price * int(quantity)
    quantity = quantity
    pizza_id = menu.id
    customer_id = customer.id
    print(pizza_id,customer_id)
    return HttpResponse('working fine')

    # a = customer.objects.all()
    # return render(request, 'customer.html', {'customers': a})
