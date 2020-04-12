from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class blogPost( models.Model ):

    user = models.ForeignKey( User , on_delete= models.DO_NOTHING )
    title = models.CharField( max_length=255 , null=True )
    post = models.TextField( null=True )
    create_at = models.DateTimeField( auto_now_add=True , null=True )