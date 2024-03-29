from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("kiran/",hello1),
    path('hello/',hello,name='hello'),
    path('',newHomePage,name = 'newHomePage'),
    path('hell03/',travelPackage,name='travelPackage'),
    path('print/',print1,name='print1'),
    path('p1/',printconsole,name='printconsole'),
    path('ran1/',random123,name='random123'),
    path('p2/',random1,name='random1'),
    path('p/',randomotp,name='randomotp'),
    path('time/',getdate1,name='getdate1'),
    path('date/',get_date,name='get_date'),
    path('tzfunctioncall/',tzfunctioncall,name='tzfunctioncall'),
    path('register/',register,name='register'),
    path('registerfunction/',registerfunction,name='registerfunction'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('ttm/',ttm,name='ttm'),
    path('weather/',weather,name='weather'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('login/',login,name='login'),
    path('login1/',login1,name='login1'),
    path('signup/',signup,name='signup'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    path('feedback/',feedback,name='feedback'),
    path('contactmail/',contactmail,name='contactmail'),
]
