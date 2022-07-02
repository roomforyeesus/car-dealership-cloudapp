from pydoc import render_doc
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
from .models import CarDealer, CarModel, CarMake
# from .restapis import related methods
from .restapis import get_dealers_from_cf, get_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
import pandas as pd


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

def djangoTemplate(request):
    context = {}
    if request.method =='GET':
        return render(request, 'djangoapp/index.html', context)
    
# Create an `about` view to render a static about page
# def about(request):
# ...
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html',context)


# Create a `contact` view to return a static contact page
#def contact(request):
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
def login_Request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/registration.html', context)
    else:
        return render(request, 'djangoapp/registration.html', context)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def logout_Request(request):
    logout(request)
    return redirect('djangoapp:index.html')


# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...
def registration_Request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return HttpResponse("djangoapp:index")

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    print ("Get Method Reached")
    context = {}
    if request.method == "GET":
        url = "https://d53467c6.us-south.apigw.appdomain.cloud/api/dealership"
        dealerships = get_dealers_from_cf(url)
        context["dealership_list"] = dealerships
        print ("hi")
        return render(request,'djangoapp/index.html',context)
# def get_dealerships(request):
#     if request.method == "GET":
#         url = "https://d53467c6.us-south.apigw.appdomain.cloud/api/dealership"
#         # Get dealers from the URL
#         dealerships = get_dealers_from_cf(url)
#         # Concat all dealer's short name
#         dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
#         # Return a list of dealer short name
#         return HttpResponse(dealer_names)

# def get_dealerships(request):
#     context={}
#     if request.method =="GET":
#         url = "https://d53467c6.us-south.apigw.appdomain.cloud/api/dealership"
        


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...


# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...


