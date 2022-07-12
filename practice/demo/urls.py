from django.urls import path
from . import views

urlpatterns = [
    # path('name', views.name, name="home"),
    path("customer", views.customer_all, name = "customer"),
    path("menu", views.menu_all, ),
    path("order", views.order_all, ),
    path("<str:hello>", views.name, name="homes"),
]