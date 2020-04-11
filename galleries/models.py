from django.db import models
from django.contrib.auth.models import User
class Location( models.Model ):
    
    location = models.CharField( max_length=200 )

    def __str__( self ):
        return self.location

class Gallery( models.Model ):

    location = models.ForeignKey( Location , on_delete=models.DO_NOTHING )
    name = models.CharField( max_length=200 )
    description = models.TextField( blank= True )
    img_1 = models.ImageField(upload_to='photo/%y/%m/%d/', blank=True)
    img_2 = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)
    img_3 = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)
    img_4 = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)
    img_5 = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)
    img_6 = models.ImageField(upload_to='photo/%y/%m/%d/',blank=True)
    is_available = models.BooleanField(default=True)
    is_published = models.BooleanField(default=True)

    def __str__( self ):
        return self.name
    def shortdesc( self ):
        return self.description[ :150 ]
    def nameUpper( self ):
        return self.name.upper()

class ServiceList( models.Model ):
    serviceName = models.CharField( max_length=20 , blank=True )
    price = models.IntegerField(default=0)

    def __str__( self ):
        return self.serviceName

class Services( models.Model ):

    servicelist = models.ForeignKey( ServiceList , on_delete=models.DO_NOTHING )
    gallery = models.ForeignKey( Gallery , on_delete=models.DO_NOTHING )

    def __str__( self ):
        return self.gallery.name

class Feedback( models.Model ):

    gallery = models.ForeignKey( Gallery , on_delete=models.DO_NOTHING )
    userinfo = models.ForeignKey( User , on_delete=models.DO_NOTHING )
    feedback = models.TextField( blank=True )

    def __str__( self ):
        return self.gallery.name