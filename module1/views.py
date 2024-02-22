import random
import string

from django.contrib.sites import requests

from .forms import *
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def hello1(request):
    return HttpResponse("<center style=color:Blue;>Welcome to TTM homepage</center>")
def hello(request):
    return render(request,'hello.html')
def newHomePage(request):
    return render(request,'newHomePage.html')

def travelPackage(request):
    return render(request,'travelPackage.html')

def print1(request):
    return render(request,'printconsole.html')
def printconsole(request):
    if request.method=="POST":
        user_input=request.POST['kiran']
        print(f'user input:{user_input}')
    'return HttpResponse(\'Form submited succesfully\')'
    a1={'user_input':user_input}
    return render(request,'printconsole.html',a1)


def random123(request):
    ran1 = ''.join(random.sample(string.digits, k=6))
    print(ran1)
    a2={'ran1':ran1}
    return render(request,'random123.html',a2)

def random1(request):
    return render(request,'randomotp.html')
def randomotp(request):
    if request.method=='POST':
        input1 = request.POST['kiran1']
        input2=int(input1)
        result_str=''.join(random.sample(string.digits,input2))
    context={'result_str':result_str}
    return render(request,'randomotp.html',context)
def getdate1(request):
    return render(request,'get_date.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']

            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form = IntegerDateForm()
        return render(request,'get_date.html',{'form':form})

def tzfunctioncall(request):
    return render(request,'pytzexample.html')

def register(request):
    return render(request,'register.html')

from .models import *
from django.shortcuts import render,redirect
def registerfunction(request):
    
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phonenumber = request.POST.get('phonenumber')
        #check if the email already exists
        if Register.objects.filter(email=email).exists():
            message1 = "Email already registered. Choose a different email"
            #return HttpResponse("Email Already exists,choose another email")
            return render(request,'register.html',{'message':message1})
        #create a new register instance and save it
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newHomePage')
    return render(request,'register.html')


import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})


def ttm(request):
    return render(request,'TTM.html')


def weather(request):
    return render(request,'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'ae7dfc38ba22c68ec55458064f955edf'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        except requests.RequestException as e:
            print(f"Error during API request: {e}")
            return render(request, 'weatherappinput.html', {'error_message': 'Failed to fetch data from the weather API. Please try again later.'})

        print(response)  # Print the response for debugging

        if response is not None:
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                temperature1 = round(temperature - 273.15, 2)
                return render(request, 'weather.html', {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
            else:
                error_message = 'City not found. Please try again.'
                return render(request, 'weatherappinput.html', {'error_message': error_message})
        else:
            error_message = 'Unexpected response from the weather API. Please try again later.'
            return render(request, 'weather.html', {'error_message': error_message})


from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def login(request):
    return render (request,'login.html')
def signup(request):
    return render (request,'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render (request,'newHomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render (request,'login.html')
    else:
        return render(request,'login.html')
def signup1(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2 = request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! USER NAME ALREADY TAKEN')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfuly!')
                return render(request,'login.html')
        else:
            messages.info(request,'password do not match')
            return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'newHomepage.html')


def feedback(request):
    return render(request,'contactus.html')

def contactmail(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend=comment +' ________________ this is just feedback form'
        data=contactus(firstname=firstname,lastname=lastname,email=email,comment=comment)
        data.save()
        return HttpResponse("<h1><center>Thank you for giving the feedback</center></h1>")