from django.shortcuts import render,redirect
from .models import User
from  .forms import *

# Create your views here.
def home(request):
    users=User.objects.all()
    context={'users':users}
    return render(request,'EBikeApp/home.html',context)

def invertorDisplay(request):
    inverters=Inverter.objects.all()
    context={'inverters':inverters}
    return render(request,'EBikeApp/displayall.html',context)

def vehicleDisplay(request):
    vehicles=vehicle.objects.all()
    context={'vehicles':vehicles}
    return render(request,'EBikeApp/vehicled.html',context)

def motorDisplay(request):
    motors=Motor.objects.all()
    context={'motors':motors}
    return render(request,'EBikeApp/motord.html',context)

def batteryDisplay(request):
    batteries=Battery.objects.all()
    context={'batteries':batteries}
    return render(request,'EBikeApp/batteryd.html',context)

def reviewDisplay(request):
    reviews=review.objects.all()
    context={'reviews':reviews}
    return render(request,'EBikeApp/reviewd.html',context)

def structureDisplay(request):
    structures=Structure.objects.all()
    context={'structures':structures}
    return render(request,'EBikeApp/structured.html',context)

def billingDetailsDisplay(request):
    billingDetailss=billingdetails.objects.all()
    context={'billingDetailss':billingDetailss}
    return render(request,'EBikeApp/billingDetails.html',context)


def user(request,pk):

    user=User.objects.get(UserId=pk)
    
    context={'user':user}
    return render(request,'EBikeApp/user.html',context)
def createuser(request):
    form=Userform()
    if request.method=='POST':
        form=Userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
        
    context={'form':form}
    return render(request,'EBikeApp/userf.html',context)

def addbattery(request):
    form=Batteryform()
    if request.method=='POST':
        form=Batteryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
        
    context={'form':form}
    return render(request,'EBikeApp/batteryf.html',context)

def addmotor(request):
    form=Motorform()
    if request.method=='POST':
        form=ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
        
    context={'form':form}
    return render(request,'EBikeApp/motorf.html',context)

def addinverter(request):
    form=Inverterform()
    if request.method=='POST':
        form=Inverterform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
        
    context={'form':form}
    return render(request,'EBikeApp/inverterf.html',context)

def addstructure(request):
    form=Structureform()
    if request.method=='POST':
        form=Structureform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
        
    context={'form':form}
    return render(request,'EBikeApp/structuref.html',context)



def addvehicle(request):
    form=Vehicleform()
    if request.method=='POST':
        form=Vehicleform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
        
    context={'form':form}
    return render(request,'EBikeApp/vehiclef.html',context)

def addreview(request):
    #print(request.User)
    form=Reviewform()
    if request.method=='POST':
        form=Reviewform(request.POST)
        if form.is_valid():
            form.save()
          
            return redirect('home')
    
        
    context={'form':form}
    return render(request,'EBikeApp/reviewf.html',context)

def addbillingDetails(request):
    form=BillingDetailsform()
    if request.method=='POST':
        form=BillingDetailsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
        
    context={'form':form}
    return render(request,'EBikeApp/billingDetailsf.html',context)


    # update function start here 
def updateUser(request,pk):
    user=User.objects.get(UserId=pk)
    form=Userform(instance=user)
    if request.method=='POST':
        form=Userform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'EBikeApp/userf.html',context)

def deleteUser(request,pk):
    user=User.objects.get(UserId=pk)
    if request.method== 'POST':
        user.delete()
        return redirect('home')
    
    
    return render(request,'EBikeApp/delete.html',{'obj':user})




