from django.db import models

class feedback( models.Model ):
    email = models.CharField(max_length=200 , null=True )
    message = models.TextField( null=True )
