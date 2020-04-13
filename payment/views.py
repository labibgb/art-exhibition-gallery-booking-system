from django.shortcuts import render, redirect
from booking.models import Booking
from galleries.models import Gallery
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from .models import Payment
def payment( request ):

    if request.method == 'POST':
        submit = request.POST['submit']
        services = request.POST.getlist('services')
        uid = request.POST['userid']
        gid = request.POST['galleryid']
        bid = request.POST['bookingid']
        stday = request.POST['startDate']
        edday= request.POST['startDate']
        total = request.POST['totalpay']
        if submit == "0":
            Booking.objects.get(pk=bid).delete()
            return redirect('galleries')
        else:
            payment = Payment( total_pay= total )
            booking = Booking.objects.get(pk=bid )
            payment.booking = booking
            gallery = Gallery.objects.get(pk=gid )
            payment.gallery = gallery
            user = User.objects.get(pk=uid)
            payment.user= user
            payment.save()
            return render( request , 'payment/makepayment.html', { 'payment' : payment } )
    return redirect('/')
def makePayment( request ):

    print("come")
    if request.method == 'POST':
        paymentid = request.POST['paymentid']
        pay = Payment.objects.get(pk=paymentid)
        pay.is_payment = True
        pay.save()
        messages.success( request , "Payment successfull")
        return redirect('/')
    return redirect('/')