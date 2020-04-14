from django.shortcuts import render, redirect
from django.contrib import messages , auth
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from payment.models import Payment
def Login( request ):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user )
            messages.success( request , "Login successfull" )
            return redirect('/')
        else:
            messages.error( request , "Username or password dosen't match.")
            return redirect('login')
    else:
        return render( request , 'user/login.html')

def register( request ):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.name = form.cleaned_data.get('name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.address = form.cleaned_data.get('address')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user )
            messages.success( request , "Registration successfull")
            return redirect('profile')
        else:
            for field in form:
                for error in field.errors:
                    messages.error( request , error)
            form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})
    return render(request, 'user/register.html', {'form':RegisterForm()})
    

def profile( request ):
    
    payment = Payment.objects.all()
    return render( request , 'user/profile.html', {'payment':payment})

def logout( request ):
    if request.method == 'POST':
        auth.logout( request )
        return redirect('/')
    return redirect('/')