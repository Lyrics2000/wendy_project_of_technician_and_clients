
from django.contrib import admin
from django.urls import path
from .views import index,clients_dashboard,technician_dashboard,Dashboard

app_name = 'mainapp'


urlpatterns = [
    path('',index, name = "index_page"),
    path('dashborad/client/',clients_dashboard,name = "client_dashbord"),
    path('dashborad/technician/',technician_dashboard,name = "technician_dashbord"),
     path('dashborad/d/',Dashboard.as_view(),name = "dashbord"),
    
   
]