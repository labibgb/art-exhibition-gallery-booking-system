from django.db import models
from galleries.models import Gallery
from django.contrib.auth.models import User

class Payment( models.Model ):
    user = models.ForeignKey( User , on_delete=models.DO_NOTHING )
    gallery = models.ForeignKey( Gallery , on_delete=models.DO_NOTHING )
    total_pay = models.IntegerField( default= 0 )
    is_payment = models.BooleanField(default=False)
    def __str__( self ):
        return self.user.username