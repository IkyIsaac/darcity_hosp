from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('appointment',views.appointment,name='appointment'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('view_doctor',views.view_doctor,name='view_doctor'),
    path('view_patient',views.view_patient,name='view_patient'),
    path('view_appointment',views.view_appointment,name='view_appointment'),
    path('delete_doctor/<int:pk>',views.delete_doctor,name='delete_doctor'),
    path('delete_patient/<int:pk>',views.delete_patient,name='delete_patient'), 
    path('delete_appointment/<int:pk>',views.delete_appointment,name='delete_appointment'), 
    path('add_doctor',views.add_doctor,name='add_doctor'),
    path('add_patient',views.add_patient,name='add_patient'),
    path('add_appointment',views.add_appointment,name='add_appointment'),
    path('update_patient',views.update_patient,name='update_patient'),
    path('look_patient',views.look_patient,name='look_patient'),

]