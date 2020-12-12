from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def clients_dashboard(request):
    return render(request,'client_dashbord.html',{})

def technician_dashboard(request):
    return render(request,'technician_dashboard.html',{})