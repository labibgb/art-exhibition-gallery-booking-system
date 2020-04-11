from django.db import models
from galleries.models import Gallery
from django.contrib.auth.models import User
# Create your models here.
class Rent( models.Model ):
    gallery = models.ForeignKey( Gallery , on_delete=models.DO_NOTHING )
    rent = models.IntegerField( default=0)

    def __str__( self ):
        return self.rent
class Payment( models.Model ):
    user = models.ForeignKey( User , on_delete=models.DO_NOTHING )
    gallery = models.ForeignKey( Gallery , on_delete=models.DO_NOTHING )
    rent = models.ForeignKey( Rent, on_delete=models.DO_NOTHING )
    is_payment = models.BooleanField(default=False)
    
    def __str__( self ):
        return self.user.username