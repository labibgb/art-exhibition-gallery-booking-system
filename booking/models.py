from django.db import models
from datetime import datetime
from galleries.models import Gallery

class Booking( models.Model ):

    gallery = models.ForeignKey( Gallery , on_delete = models.DO_NOTHING )
    booking_date = models.DateField( default = datetime.now , blank = True)
    end_date = models.DateField( default = datetime.now , blank = True )
    def __str__( self ):
        return self.gallery.name