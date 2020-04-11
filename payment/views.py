from django.shortcuts import render, redirect

# Create your views here.
def payment( request ):

    if request.method == 'POST':
        return render( request , 'payment/payment.html')
    return redirect('/')