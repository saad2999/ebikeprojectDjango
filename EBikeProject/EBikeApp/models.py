from django.db import models

# from django.contrib.auth.models import User



# Create your models here.
class User(models.Model):
    UserId=models.AutoField(null=False, unique=True,primary_key=True)
    Fname=models.CharField(max_length=20)
    Lname=models.CharField(max_length=20)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    Gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    Email=models.EmailField(max_length=50)
    contact_number=models.CharField(max_length=15)
    def __str__(self): 
        return str(self.UserId)
   
    
class Battery(models.Model):
    batteryID= models.AutoField(null=False,unique=True,primary_key=True)
    batteryTYPE= models.CharField(max_length=10) 
    volts= models.IntegerField(default=0)
    Watthour =models.IntegerField(default=0)
    lifetime =models.IntegerField(default= 0)

class Motor(models.Model):
    motorID=models.AutoField(null=False,unique=True,primary_key=True) 
    motorTYPE =models.CharField(max_length=10) 
    placement=models.CharField(max_length=10) 
    Wattage=models.IntegerField(default= 0)
    volts=models.IntegerField(default=0)
    manufacturer=models.CharField(max_length=10) 

class Structure (models.Model):
    structureID=models.AutoField(null=False,unique=True,primary_key=True)
    frame=models.CharField(max_length=10)
    payloadCAP =models.IntegerField(max_length=10)
    color=models.CharField(default='red',max_length=10)



class Inverter(models.Model):
    inverterID=models.AutoField(null=False,unique=True,primary_key=True)
    Wattage=models.IntegerField(max_length=10)
    volts=models.IntegerField(max_length=10)


class vehicle(models.Model):
    user=models.ForeignKey(User,on_delete=models.RESTRICT)
    battery=models.ForeignKey(Battery,on_delete=models.RESTRICT)
    motor=models.ForeignKey(Motor,on_delete=models.RESTRICT)
    inverter=models.ForeignKey(Inverter,on_delete=models.RESTRICT)
    structure=models.ForeignKey(Structure,on_delete=models.RESTRICT)
    vehicleTYPE=models.CharField(max_length=10)
    weightKG=models.IntegerField(default=0)
    OrderDATE=models.DateTimeField()
    warrantyDATE=models.DateTimeField()
    tyre=models.CharField(max_length=10)
    helmet=models.CharField(max_length=10)
    pedal=models.CharField(max_length=10)
    meter=models.CharField(max_length=10)

class review(models.Model):
    user=models.ForeignKey(User,on_delete=models.RESTRICT)
    vehicle=models.ForeignKey(vehicle,on_delete=models.RESTRICT)
    reviewTEXT=models.CharField(max_length=50)



class billingdetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.RESTRICT)
    #declare userid as composite key with billingdetailid
    address=models.CharField(max_length=50)
    country=models.CharField(max_length=15)
    zip=models.IntegerField(default=0)
    CCno=models.IntegerField(default=0)
    promocode=models.CharField(max_length=10)


 

