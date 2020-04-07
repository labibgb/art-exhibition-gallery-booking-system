from django.contrib import admin

from .models import Booking

class bookingAdmin( admin.ModelAdmin ):
    list_display = ('id' , 'gallery', 'booking_date', 'end_date' )
    list_display_links = ( 'id' , 'gallery')
    list_filter = ( 'gallery',)
    #list_editable = (, , )
    #search_fields = ( , , )
    list_per_page = 20

admin.site.register( Booking , bookingAdmin)