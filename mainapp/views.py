from django.shortcuts import render,redirect
from .forms import TechnicianDetailss
from .models import TechnicianDetails
from django.views.generic import DetailView,View,ListView
from accounts.models import CustomUser
from .models import ProductTech
# Create your views here.
def index(request):
    return render(request,'index.html',{})

def clients_dashboard(request):
    return render(request,'client_dashbord.html',{})


class Dashboard(View):
    def get(self,request,*args,**kwargs):
        
        allproducts = ProductTech.objects.all()
        
        context = {
            'products' : allproducts,
            
        }
    
        return render(request,'dashboard.html',context)

def technician_dashboard(request):
    form = TechnicianDetailss(request.POST or None)
    context = {
        'form' : form
    }
    if form.is_valid:
        if request.POST:
            ShopLocation = request.POST.get("Shoplocation")
            PhoneNumber = request.POST.get("PhoneNumber")

            Description = request.POST.get("Description")
            
            emaill  = request.session.get('mtech_id')
            user_id_for_technician = CustomUser.objects.get(email__iexact=emaill)
            print(user_id_for_technician)
            userMoreDetails = TechnicianDetails(TechnicianId = user_id_for_technician,ShopLocation = ShopLocation,PhoneNumber = PhoneNumber, Description = Description)
            userMoreDetails.save()
            
            del request.session['mtech_id']
            
            return redirect("mainapp:dashbord")
    return render(request,'technician_dashboard.html',context)