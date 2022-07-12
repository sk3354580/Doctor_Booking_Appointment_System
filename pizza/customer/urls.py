from django.urls import path
from  customer import views

urlpatterns = [
    
    path('customer',views.client),
    path('',views.admin),
    path('orders',views.order_all)
]
