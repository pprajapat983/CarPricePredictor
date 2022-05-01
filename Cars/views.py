from math import ceil, floor
from django.shortcuts import render
from .models import car
import pickle
import pandas as pd
import numpy as np

# Create your views here.
def index(request):
    cars=car.objects.all()
    return render(request, 'Cars/index.html',{'cars':cars})


def about(request):
    return render(request, 'Cars/about.html')

def sell(request):
    return render(request, 'Cars/about.html')

def predict(request):
    # load the model
    name='Maruti Suzuki Swift'
    company='Maruti'
    year=2019
    kms_driven=100
    fuel_type='Petrol'
    pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
    a=pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array([name,company,year,kms_driven,fuel_type]).reshape(1,5)))
    # ts = a.tostring()
    print(type(a[0]))
    # print(type(ts))
    return render(request, 'Cars/calculatesp.html',{'a':ceil(a[0])})
        

def contact(request):
    thank = False
    if request.method == "POST":
        con_name = request.POST.get('name', '')
        con_email = request.POST.get('email', '')
        con_phone = request.POST.get('phone', '')
        con_desc = request.POST.get('desc', '')
        # print(name,email,phone,desc)
        mycontact = Contact(name=con_name, email=con_email,
                            phone=con_phone, desc=con_desc)
        mycontact.save()
        messages.success(request,"Your details successfully submited !" )
    return render(request, "shop/contact.html",)
