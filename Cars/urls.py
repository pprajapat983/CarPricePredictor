"""Cars24x7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="Home"),
    path("buy/",views.buypage,name="Buy"),
    path("about/",views.about,name="AboutUs"),
    path("predict/",views.predict,name="PredictSP"),
    path("contact/",views.contact,name="Contact"),
    path("search/",views.search,name="Search"),
    path("sell/",views.sellcar,name="SellCar"),
    path("carview/<int:carid>",views.carview,name="Carview"),
    path('login/',views.handleLogin,name='login'),
    path('logout/',views.handleLogout,name='logout'),    
]
