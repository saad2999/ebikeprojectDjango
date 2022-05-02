from django.forms import ModelForm
from .models import *
from .models import Motor as motorf



class Userform(ModelForm):
    class Meta:
        model=User
        fields= '__all__'
class Batteryform(ModelForm):
    class Meta:
        model=Battery
        fields= '__all__'

class Motorform(ModelForm):
    class Meta:
        model=motorf
        fields= '__all__'

class Inverterform(ModelForm):
    class Meta:
        model=Inverter
        fields= '__all__'

class Structureform(ModelForm):
    class Meta:
        model=Structure
        fields= '__all__'

class Vehicleform(ModelForm):
    class Meta:
        model=vehicle
        fields= '__all__'

class Reviewform(ModelForm):
    class Meta:
        model=review
        fields= '__all__'




class BillingDetailsform(ModelForm):
    class Meta:
        model=billingdetails
        fields= '__all__'
       

