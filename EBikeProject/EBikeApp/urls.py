from django.urls import path
from . import views



urlpatterns=[
    path('', views.home ,name="home"),
    path('create-user/', views.createuser ,name="create-user"),
    path('user/<int:pk>/', views.user,name="user"),
    path('add-battery/',views.addbattery,name="add-battery"),
    path('add-motor/',views.addmotor,name="add-motor"),
    path('add-inverter/',views.addinverter,name="add-inverter"),
    path('add-structure/',views.addstructure,name="add-structure"),
    path('add-vehicle/',views.addvehicle,name="add-vehicle"),
    path('add-review/',views.addreview,name="add-review"),
    path('add-billingDetails/',views.addbillingDetails,name="add-billingDetails"),
    path('update-user/<int:pk>/', views.updateUser ,name="update-user"),
    path('delete-user/<int:pk>/', views.deleteUser ,name="delete-user"),
    path('Display-invertor/', views.invertorDisplay ,name="Display-invertor"),
    path('Display-vehicle/', views.vehicleDisplay ,name="Display-vehicle"),
    path('Display-motor/', views.motorDisplay ,name="Display-motor"),
    path('Display-battery/', views.batteryDisplay ,name="Display-battery"),
    path('Display-review/', views.reviewDisplay ,name="Display-review"),
    path('Display-structure/', views.structureDisplay ,name="Display-structure"),
    path('Display-billingDetails/', views.billingDetailsDisplay ,name="Display-billingDetails"),
]