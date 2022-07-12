from cgi import print_exception
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect

from . models import customer, menu,order
# def home(request):
#     return render(request,'admin.html')
def admin(request):
    if request.method == 'POST':
        if request.POST.get('pname') and request.POST.get('quantity') and request.POST.get('price') and request.POST.get('type'):
            post = menu()
            post.pname = request.POST.get('pname')
            post.is_veg = request.POST.get('type')
            global quantity
            quantity = request.POST.get('quantity')
            post.quantity = request.POST.get('quantity')
            global price 
            price = request.POST.get('price')
            post.price = request.POST.get('price')
            post.save()
            names = menu.objects.all()
            data = {
                    'names': names
                }

            return render(request, 'admin.html',data)
            # return redirect('show')

    else:
        return render(request, 'admin.html')
# def show(request):

#     names = menu.objects.all()
#     data = {
#         'names': names
#     }
#     return render(request,'admin.html',data)
def client(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('address'):
            post = customer()
            post.name = request.POST.get('name')
            post.phone = request.POST.get('phone')
            post.address = request.POST.get('address')
            
            post.save()
            pate = customer.objects.all()
            data = {
                    'nam': pate
                }
            return render(request,'client.html',data)
    else:
        return render(request,'client.html')
# def view(request):

#     pate = customer.objects.all()
#     data = {
#         'nam': pate
#     }
#     return render(request,'client.html',data)

def order_all(request):
    ord = order.objects.all()
    if request.method =="POST":
        o = order(customer_id = customer.id,pizza_id = menu.id, quantity = quantity, total_amount = price * int(quantity))
        o.save()
        return HttpResponse('working fine')
    else:
        return render(request,'order.html',{'ord':ord})