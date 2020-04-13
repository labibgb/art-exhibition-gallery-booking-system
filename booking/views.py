from django.shortcuts import render, redirect
from .models import Exebition, TimeSlot, Booking
from django.contrib.auth.models import User
from galleries.models import Gallery, ServiceList
def book( request ):
    if request.method=='POST':
        serviceList = ServiceList.objects.all()
        userid = request.POST['userid']
        galleryid = request.POST['galleryid']
        time = request.POST['time']
        exhibition = request.POST['exhibition']
        bookingDate = request.POST['bookingDate']
        endDate = request.POST['endDate']
        makebooking = Booking( booking_date= bookingDate,end_date = endDate)
        gallery = Gallery.objects.get( pk=galleryid )
        makebooking.gallery = gallery
        user = User.objects.get( pk= userid )
        makebooking.userinfo = user
        exiname = Exebition.objects.get(pk=exhibition)
        makebooking.exebition = exiname
        tslot = TimeSlot.objects.get(pk=time)
        makebooking.TimeSlot = tslot
        makebooking.save()

        context = {
            'booking' : makebooking,
            'servicelist' : serviceList
        }
        return render( request , 'payment/payment.html' , context )
    
    return redirect( '/' )