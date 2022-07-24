from django.urls import path
from .views import *

urlpatterns = [
    path('',BlogsListview.as_view(),name='BlogListview'),
    path('blogsdetailview/<int:pk>',BlogsDetailview.as_view(),name='BlogsDetailview'),
    path('blogscreateview',BlogsCreateview.as_view(),name='blogscreateview'),
    path('blogsupdateview/<int:pk>',BlogsUpdateview.as_view(),name='blogsupdateview'),
    path('blogsdeleteview/delete/<int:pk>',BlogsDeleteview.as_view(),name='blodsdeleteview')

]
