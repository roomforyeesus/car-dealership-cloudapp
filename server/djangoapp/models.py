from datetime import datetime
from distutils.archive_util import make_archive
from operator import truediv
from sre_parse import State
from tkinter import CASCADE
from unicodedata import name
try:
    from django.db import models
except Exception:
    print("there was an error loading django modules. do you have django installed?")
    sys.exit()
from django.utils.timezone import now
from django.conf import settings
import uuid

# Create your models here.
# User model
class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    email = models.CharField(null=False, max_length=80, default='example@email.com')
    dob = models.DateField(null=True)
    
    # Create a toString method for object string representation
    def __str__(self):
        return "Hi,"+ self.first_name + " " + self.last_name

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=80, default='Joe Mama')
    make = models.CharField(null=False, max_length=30, default='mazdaradi')
    model = models.CharField(null=False, max_length=30, default='HC1')
    year = models.IntegerField(null=False, max_length=4, default='1993')
    dealership = models.IntegerField(null=False, max_length=5, default='input dealership id here')
    #purchased = models.CharField(null=False, max_length=2, choices=yesno.choices, default='NO')
    #p_date =  datetime.models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
    review = models.CharField(null=False, max_length=250, default="Write Reviews Here")
    
    def __str__(self):
        print (self)


    


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    name = models.CharField(null=False, max_length=80, default='Joe Mama')
    make = models.CharField(null=False, max_length=30, default='mazdaradi')
    model = models.CharField(null=False, max_length=30, default='HC1')
    year = models.IntegerField(null=False, max_length=4, default='1993')
    dealership = models.IntegerField(null=False, max_length=5, default='input dealership id here')
    #purchased = models.CharField(null=False, max_length=2, choices=yesno.choices, default='NO')
    #p_date =  datetime.models.DateTimeField(_(""), auto_now=False, auto_now_add=False)
    review = models.CharField(null=False, max_length=250, default="Write Reviews Here")
    
    def __str__(self):
        return(self)
# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, state, full_name, id, lat, long, short_name, st, zip):  
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer state
        self.state = state
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return  "Full Name: " + self.full_name +\
                "Short Name: " + self.short_name +\
                "ID: " + self.id +\
                "Address: " + self.address +\
                "City: " + self.city +\
                "State: " + self.state +\
                "ST: " + self.st +\
                "Zip: " + self.zip +\
                "Longitude: " + self.long +\
                "Latitude: " + self.lat

# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview:
    def __init__(self, car_make, car_model, car_year, dealership, id, name, purchase, purchase_date, review):
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.dealership = dealership
        self.id = id
        self.name = name
        self.purchase = purchase
        self.purchase_date = purchase_date
        self.review = review
    def __str__(self):
        return "Car Make: " + self.car_make +\
                "Car Model: " + self.car_model +\
                "Car Year: " + self.car_year +\
                "Dealership ID: " + self.dealership +\
                "Name of Buyer: " + self.name +\
                "Purchase: " + self.purchase +\
                "Purchase Date: " + self.purchase_date +\
                "Review ID: " + self.id +\
                "Review: " + self.review