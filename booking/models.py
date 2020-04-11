from django.db import models
from datetime import datetime
from galleries.models import Gallery
from django.contrib.auth.models import User

class Exebition( models.Model ):
    exebitionType = models.CharField( max_length=100, blank=True )

    def __str__( self ):
        return self.exebitionType
class TimeSlot( models.Model ):
    timest = models.TextField( null=True)
    timeed = models.TimeField( null=True)
    
    def get_time_st( self ):
        return str( self.timest )

    def get_time_ed( self ):
        return str( self.timeed )

class Booking( models.Model ):

    gallery = models.ForeignKey( Gallery , on_delete = models.DO_NOTHING )
    exebition = models.ForeignKey( Exebition , on_delete = models.DO_NOTHING )
    TimeSlot = models.ForeignKey( TimeSlot , on_delete = models.DO_NOTHING )
    userinfo = models.ForeignKey( User , on_delete = models.DO_NOTHING )
    booking_date = models.DateField( default = datetime.now , blank = True)
    end_date = models.DateField( default = datetime.now , blank = True )
    def __str__( self ):
        return self.gallery.name