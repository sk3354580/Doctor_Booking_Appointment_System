from django.urls import  path
from . import  views
urlpatterns = [
    path('',views.index, name="index"),
    path('admins',views.admins, name="admins"),
    path('doctors',views.doctors, name="doctors"),
    path('patients',views.patients, name="patients"),
    path('do_admin_signup', views.do_admin_signup, name="do_admin_signup"),
    path('do_doctor_signup', views.do_doctor_signup, name="do_doctor_signup"),
    path('do_patient_signup', views.do_patient_signup, name="do_patient_signup"),
    path('logins',views.logins,name="logins"),
    path('doLogin',views.doLogin,name="doLogin"),

]