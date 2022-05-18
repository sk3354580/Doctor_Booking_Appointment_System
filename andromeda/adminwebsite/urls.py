from django.urls import path
from . import views
urlpatterns = [
    path('admin', views.admine ,name ="admine"),
    path('appointment-list', views.appointment_list ,name ="appointment_list"),
    path('blank-pagew', views.blank_pagew ,name ="blank_pagew"),
    path('componentsw', views.componentsw ,name ="componentsw"),
    path('data-tables', views.data_tables ,name ="data_tables"),
    path('doctor-list', views.doctor_list ,name ="doctor_list"),
    path('error-404', views.error_404 ,name ="error_404"),
    path('error-500', views.error_500 ,name ="error_500"),
    path('forgot-passwordw', views.forgot_passwordw ,name ="forgot_passwordw"),
    path('form-basic-inputs', views.form_basic_inputs ,name ="form_basic_inputs"),
    path('form-horizontal', views.form_horizontal ,name ="form_horizontal"),
    path('form-input-groups', views.form_input_groups ,name ="form_input_groups"),
    path('form-mask', views.form_mask ,name ="form_mask"),
    path('form-validation', views.form_validation ,name ="form_validation"),
    path('form-vertical', views.form_vertical ,name ="form_vertical"),
    path('invoice-report', views.invoice_report ,name ="invoice_report"),
    path('invoice', views.invoice ,name ="invoice"),
    path('lock-screen', views.lock_screen ,name ="lock_screen"),
    path('loginw', views.loginw ,name ="loginw"),
    path('patient-list', views.patient_list ,name ="patient_list"),
    path('profilew', views.profilew ,name ="profilew"),
    path('registerw', views.registerw ,name ="registerw"),
    path('reviewsw', views.reviewsw ,name ="reviewsw"),
    path('settings', views.settings ,name ="settings"),
    path('specialities', views.specialities ,name ="specialities"),
    path('table-basic', views.table_basic ,name ="table_basic"),
    path('transactions-list', views.transactions_list ,name ="transactions_list"),
    path('logout',views.logout,name="logout"),
]