from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile

class userAdmin( admin.ModelAdmin ):
    search_fields = ( 'email' , )
    list_display_links = ( 'id', 'name', )
    list_display = ( 'id' , 'name' , 'email' , 'phone' , 'address' , )
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = (
        ('Personal info', {'fields': ('name' ,'email', 'phone' , 'address', 'blogpost' )}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    ordering = ('email',)
    filter_horizontal = ()
    list_per_page = 20

admin.site.register( Profile , userAdmin )
