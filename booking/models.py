from django.db import models
from datetime import datetime
from galleries.models import Gallery
from user.models import InfoTable

class Exebition( models.Model ):
    exebitionType = models.CharField( max_length=100, blank=True )

    def __str__( self ):
        return self.exebitionType
class TimeSlot( models.Model ):
    slot = models.IntegerField(default=0, null=True )
    time = models.TimeField(auto_now=True)
    
class Booking( models.Model ):

    gallery = models.ForeignKey( Gallery , on_delete = models.DO_NOTHING )
    exebition = models.ForeignKey( Exebition , on_delete = models.DO_NOTHING )
    TimeSlot = models.ForeignKey( TimeSlot , on_delete = models.DO_NOTHING )
    userinfo = models.ForeignKey( InfoTable , on_delete = models.DO_NOTHING )
    booking_date = models.DateField( default = datetime.now , blank = True)
    end_date = models.DateField( default = datetime.now , blank = True )
    def __str__( self ):
        return self.gallery.name