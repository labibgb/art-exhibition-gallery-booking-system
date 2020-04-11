from django.shortcuts import render, redirect
from .models import Exebition, TimeSlot, Booking
def book( request ):
    exhibition = Exebition.objects.all()
    timeslot = TimeSlot.objects.all()
    context = {
        'exebition' : exhibition,
        'timeslot' : timeslot
    }
    if request.method=='POST':
        userid = request.POST['userid']
        galleryid = request.POST['galleryid']
        time = request.POST.getlist('time')
        exhibition = request.POST.getlist('exhibition')
        bookingDate = request.POST['bookingDate']
        endDate = request.POST['endDate']
        for time in time:
            user = 

        print( userid , galleryid , time , exhibition , bookingDate , endDate )
    return render( request , 'partials/booking.html', context )