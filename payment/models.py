from django.db import models
from galleries.models import Gallery
from django.contrib.auth.models import User
from booking.models import Booking

class Payment( models.Model ):
    user = models.ForeignKey( User , on_delete=models.CASCADE )
    gallery = models.ForeignKey( Gallery , on_delete=models.CASCADE )
    booking = models.OneToOneField( Booking , on_delete=models.CASCADE)
    total_pay = models.IntegerField( default= 0 )
    is_payment = models.BooleanField(default=False)
    def __str__( self ):
        return self.user.username