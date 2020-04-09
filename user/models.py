from django.db import models
from datetime import datetime
# Create your models here.

class InfoTable( models.Model ):

    name = models.CharField( max_length=50 , blank=True)
    email = models.CharField( max_length=50 , blank=True)
    phone = models.CharField( max_length=20  , blank=True)
    address = models.CharField( max_length=50 , blank=True )
    password = models.CharField( max_length=200 , blank=True)
    is_available = models.BooleanField(default=True, blank=True)

    def __str__( self ):
        return self.name