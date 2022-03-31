from django.shortcuts import *
from django.http import *
from django.urls import *
from . import models, logger
from django.utils import timezone
import datetime
import re

##########################################
#	HOME VIEW
##########################################
#	Takes a request then returns a rendered version of the html template named 'index'
def home(request):
    return render(request, 'shopping/home.html', {})

##########################################
#	LOGIN VIEW
##########################################
#	Takes a request then returns a rendered version of the html template named 'login'
def login(request):
    return render(request, 'shopping/login.html', {})

##########################################
#	LOGIN REQUEST
##########################################
#	Takes a request to log in
#	Tries each person model to log into if user and password are correct.
#	If the login is unsucessful print an error and return to same urlresolvers
#	If the login is successful, log in to the corresponding model account
def loginSubmit(request):
    try:
        user = models.Customer.objects.get(
            userName=request.POST['username'])  # applies username to current person attempting to log in.
        if request.POST['password'] != user.password:  # If the password they answer does not match on file password
            return render(request, 'shopping/login.html', {'error_message': "Password does not match"})
        logger.write(timezone.now(), user.userName, "LOGIN", " Customer " + user.userName + " logged in.")
        return HttpResponseRedirect(
            reverse('shopping:pinfo', kwargs={'pid': request.POST['username']}))  # sends them to pinfo page
    except models.Customer.DoesNotExist:
        pass

    try:
        user = models.Administrator.objects.get(userName=request.POST['username'])
        if request.POST['password'] != user.password:
            return render(request, 'shopping/login.html', {'error_message': "Password does not match"})
        logger.write(timezone.now(), user.userName, "LOGIN", " Admin " + user.userName + " logged in.")
        return HttpResponseRedirect(
            reverse('shopping:ainfo', kwargs={'aid': request.POST['username']}))
    except models.Administrator.DoesNotExist:
        pass

    return render(request, 'shopping/login.html', {'error_message': "Username not found"})

##########################################
#	USER REGISTER VIEW
##########################################
#	Takes a request then returns a rendered version of the html template named 'register'
def signup(request):
    return render(request, 'shopping/signup.html', {})


##########################################
#	REGISTER CUSTOMER
##########################################
#	Takes a request.
#	Logic to create a customer.
#	Try to find other users with the same name for each model.
#	If same username, throw error. Else pass with success
def signupSubmit(request):
    try:
        models.Customer.objects.get(name=request.POST['name'])
        return render(request, 'shopping/signup.html',
                      {'error_message': "Name already exists", 'shoppings': models.Company.objects})
    except models.Customer.DoesNotExist:
        pass

    try:
        models.Administrator.objects.get(name=request.POST['name'])
        return render(request, 'shopping/signup.html',
                      {'error_message': "Name already exists", 'shoppings': models.Company.objects})
    except models.Administrator.DoesNotExist:
        pass

    if not re.match(r"^\w+$", request.POST['name']):
        return render(request, 'shopping/signup.html',
                      {'error_message': "Name is invalid", 'shoppings': models.Company.objects})

    if not request.POST['password']:
        return render(request, 'shopping/signup.html',
                      {'error_message': "Password cannot be empty", 'shoppings': models.Company.objects})

    email = None
    if request.POST['email']:
        email = models.Email(email=request.POST['email'])
        email.save()

    phoneNumber = None
    if request.POST['phoneNumber']:
        phoneNumber = models.PhoneNumber(phoneNumber=request.POST['phoneNumber'])
        phoneNumber.save()

    user = models.Customer(
        name=request.POST['name'],
        password=request.POST['password'],
        phoneNumber=phoneNumber,
        email=email,
    )
    user.save()

    logger.write(timezone.now(), user.userName, "SIGNUP", " Customer " + user.userName + " was signed up.")

    return HttpResponseRedirect(reverse('shopping:pinfo', kwargs={'pid': request.POST['username']}))