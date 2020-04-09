from django.shortcuts import render, redirect
from django.contrib import messages , auth
from .models import InfoTable
from django.contrib.auth import hashers
from django.contrib.auth.models import User
def login( request ):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        usr = auth.authenticate( username=email , password=password)
        if usr is not None:
            user = InfoTable.objects.filter( email=email )
            auth.login(request , user )
            messages.success( request , 'You are logged in')
            return redirect('profile', user)
        else:
             messages.error( request , 'Incorrect email or password')
             return redirect('login')

    else:
        return render( request , 'user/login.html')

def register( request ):

    if request.method == 'POST':
        #get data form register form
        name = request.POST['fname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        cPassword = request.POST['confirmPassword']

        if password == cPassword:
            if InfoTable.objects.filter(email=email).exists():
                messages.error( request , 'That email is begin used.')
                return redirect('register')
            else:
                user = InfoTable.objects.create( name = name , email=email, phone=phone, address=address, password=password )
                urs = User.objects.create_user( username=email , password = password )
                messages.success( request, "You are logged in.")
                return redirect('login')
        else:
            messages.error( request , 'Passwors do not match.')
            return redirect('register') 
    else:
        return render( request , 'user/register.html')

def profile( request ):

    return render( request , 'user/profile.html')

def logout( request ):

    return redirect('/')