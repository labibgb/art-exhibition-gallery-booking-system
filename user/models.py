from django.db import models
from datetime import datetime
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager( BaseUserManager ):

    def create_user( self , email , password = None , is_staff=False, is_admin=False, is_active = True , name = None , phone = None , address = None ):
        if not email:
            raise ValueError("User must have an email address")
        user_obj = self.model( 
            email = self.normalize_email( email ),
            name = name,
            phone = phone,
            address = address
        )
        user_obj.set_password( password )
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.save( using = self._db )
        return user_obj
    
    def create_staffuser( self , email , password=None ):

        user = self.create_user( email, password = password, is_staff=True )
        return user


    def create_superuser( self , email , password=None ):

        user = self.create_user( email, password = password ,is_staff=True, is_admin=True)
        return user

    


class User( AbstractBaseUser ):

    email = models.EmailField( default='abc@email.com', max_length=255 , unique=True , null=True)
    active = models.BooleanField( default=True)
    admin = models.BooleanField( default=False )
    staff = models.BooleanField( default=False )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    userManager = UserManager()

    def __str__( self ):
        return self.email

    def has_perm( self , perm , obj = None ):
        return True
    def has_module_perms( self , app_label ):
        return True
    @property
    def is_staff( self ):
        return self.staff
    @property
    def is_admin( self ):
        return self.admin

    @property
    def is_active( self ):
        return self.active
    

class InfoTable( models.Model ):

    name = models.CharField( max_length=50 , blank=True)
    email = models.CharField( max_length=50 , blank=True)
    phone = models.CharField( max_length=20  , blank=True)
    address = models.CharField( max_length=50 , blank=True )
    password = models.CharField( max_length=200 , blank=True)
    active = models.BooleanField( default=False, null= True )
    def __str__( self ):
        return self.name

    def get_shot_name( self ):
        return self.name.split(' ')[ 0 ]