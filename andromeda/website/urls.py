from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="index"),
    path('add-billing',views.addbilling, name="addbilling"),
    path('add-prescription',views.addprescription, name="addprescription"),
    path('appointments',views.appointments,name="appointments"),
    path('blank-page',views.blankpage, name="blankpage"),
    path('booking',views.booking, name="booking"),
    path('booking-success',views.bookingsuccess, name="bookingsuccess"),
    path('calendar',views.calender, name="calender"),
    path('change-password',views.changepassword, name="changepassword"),
    path('chat',views.chat, name="chat"),
    path('chat-doctor',views.chatdoctor, name="chatdoctor"),
    path('checkout',views.checkout, name="checkout"),
    path('components',views.components, name="components"),
    path('doctor-change-password',views.doctorchangepassword, name="doctorchangepassword"),
    path('doctor-dashboard',views.doctordashboard, name="doctordashboard"),
    path('doctor-profile',views.doctorprofile, name="doctorprofile"),
    path('doctor-profile-settings',views.doctorprofilesettings, name="doctorprofilesettings"),
    path('doctor-register',views.doctorregister, name="doctorregister"),
    path('edit-billing',views.editbilling, name="editbilling"),
    path('edit-prescription',views.editprescription, name="editprescription"),
    path('favourites',views.favourites, name="favourites"),
    path('forgot-password',views.forgotpassword, name="forgotpassword"),
    path('index-2',views.index2, name="index2"),
    path('invoice-view',views.invoiceview, name="invoiceview"),
    path('invoices',views.invoices, name="invoices"),
    path('login',views.login,name="login"),
    path('my-patients',views.mypatients, name="mypatients"),
    path('patient-dashboard',views.patientdashboard, name="patientdashboard"),
    path('profile-settings',views.patientprofilesettings, name="patientprofilesettings"),
    path('privacy-policy',views.privacypolicy, name="privacypolicy"),
    path('patient-profile',views.patientprofile, name="patientprofile"),
    path('register',views.register, name="register"),
    path('reviews',views.reviews, name="reviews"),
    path('schedule-timings',views.scheduletimings, name="scheduletimings"),
    path('search',views.search, name="search"),
    path('social-media',views.socialmedia, name="socialmedia"),
    path('term-condition',views.termcondition, name="termcondition"),
    path('video-call',views.videocall, name="videocall"),
    path('voice-call',views.voicecall, name="voicecall"),

    path('all_doctors', views.all_doctors, name="all_doctors"),
    path('doctor_info/<int:ids>', views.doctor_info, name="doctor_info"),
    path('doctor-edit/<int:id>', views.doctor_edit, name="doctor-edit"),
    path('doctor-delete/<int:id>', views.doctor_delete, name="doctor-delete"),

]