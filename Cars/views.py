from email.mime import image
from math import ceil, floor
from operator import contains
from unicodedata import name
from django.shortcuts import render,redirect
from markupsafe import re

import Cars
from .models import car,Contact
import pickle
import pandas as pd
import numpy as np
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse


# Create your views here.
def index(request):
    #cars=car.objects.all()
    return render(request, 'Cars/index.html')

def buypage(request):
    cars=car.objects.all()
    return render(request, 'Cars/buy.html',{'cars':cars})

def about(request):
    return render(request, 'Cars/about.html')

def carview(request,carid):
    car_req = car.objects.filter(id=carid)
    # print(carid)
    print(car_req)
    # print(car_req)
    return render(request, 'Cars/carview.html',{'car':car_req.first})    

def sellcar(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        car_type = request.POST.get('company', '')
        year = request.POST.get('year', '')
        selling_price=request.POST.get('selling_price','')
        phone = request.POST.get('phone', '')
        kms_driven = request.POST.get('kms', '')
        fuel_type=request.POST.get('fueltype','')
        owner=request.POST.get('fueltype','')
        images=request.FILES
        print(images)
        image=images.get('carimage')
        newcar = car(car_name=name, car_type=car_type,
                            phone=phone, year=year,kms_driven=kms_driven,fuel_type=fuel_type,owner=owner,image=image,selling_price=selling_price)
        newcar.save()
    return render(request, 'Cars/Sell.html')

def predict(request):
    #load the model
    if request.method == "POST":
        name = request.POST.get('name','')
        print(name)
        company = request.POST.get('company', '')
        print(company)
        year = request.POST.get('year', '')
        kms_driven = request.POST.get('kms', '')
        fuel_type=request.POST.get('fueltype','')
        pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
        a=pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array([name,company,year,kms_driven,fuel_type]).reshape(1,5)))
        # ts = a.tostring()
        # print((a[0]))
        # print(type(ts))
        return render(request, 'Cars/calculatesp.html',{'a':ceil(a[0]),'carname':name})
    return render(request, 'Cars/calculatesp.html')

    # name='Ford Figo'
    # company='Maruti'
    # year=2019
    # kms_driven=100
    # fuel_type='Petrol'
    # pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
    # a=pipe.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array([name,company,year,kms_driven,fuel_type]).reshape(1,5)))
    # # ts = a.tostring()
    # print(type(a[0]))
    # # print(type(ts))
    # return render(request, 'Cars/calculatesp.html',{'a':ceil(a[0])})
        

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
         
    return render(request, "Cars/contact.html",)

def search(request):
    if request.method == "POST":
        srch = request.POST.get('srch', '')
        cars_req=[]
        for carobj in car.objects.all():
            if carobj.car_name.__contains__(srch):
                cars_req.append(carobj)
        return render(request, 'Cars/buy.html',{'cars':cars_req})  
        # print(name,email,phone,desc)
    return render(request, "Cars/home.html")



def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,f' Welcome {loginusername}, Your are successfully Logged In!')
            return redirect('/')
        else:
            messages.error(request,"Invalid credentials, Please try again !")
            return redirect('/')
       
    return HttpResponse('404- Not Found')



def handleLogout(request):
    logout(request)
    messages.success(request,"Your are successfully Logged Out !" )
    return redirect('/')