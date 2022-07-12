from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('todoitems/<int:id>',views.todoitems,name="todoitems"),
    path('task_delete/<int:id>',views.task_delete,name="task_delete"),
    path('alldata/<int:id>',views.alldata,name="alldata"),


]


