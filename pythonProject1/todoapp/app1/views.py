from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect,reverse
from . models import *
# Create your views here.
def index(request):
    alltasks = todotitle.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        saveallvalues = todotitle(
            title = title
        )
        saveallvalues.save()
        return render(request,'index.html', {'alltasks':alltasks})
    else:
        return render(request,'index.html', {'alltasks':alltasks})
def todoitems(request,id):

    title_id = todotitle.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        allitems = todolist(
            title = title,
            description = description,
            todo_list = title_id
        )
        allitems.save()

        return redirect('alldata',id =id)

    else:
        return render(request,'items.html',{'id':id })

def task_delete(request, id):
    title_delete = todotitle.objects.get(id=id)
    title_delete.delete()
    return HttpResponseRedirect(reverse('index'))
def alldata(request,id):
    alldata = todolist.objects.get(todo_list=id)
    return render(request,'alldata.html',{'alldata':alldata})