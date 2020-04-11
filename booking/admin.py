from django.contrib import admin

from .models import Booking, Exebition, TimeSlot

class bookingAdmin( admin.ModelAdmin ):
    list_display = ('id' , 'gallery', 'booking_date', 'end_date' , 'userinfo' , 'TimeSlot' , 'exebition' )
    list_display_links = ( 'id' , 'gallery')
    list_filter = ( 'gallery',)
    #list_editable = (, , )
    #search_fields = ( , , )
    list_per_page = 20
class timeslot( admin.ModelAdmin ):
    list_display = ('id' , 'timest', 'timeed' )
    list_display_links = ( 'id' ,)
    #list_editable = (, , )
    #search_fields = ( , , )
    list_per_page = 20

class exhibition( admin.ModelAdmin ):
    list_display = ('id' , 'exebitionType',  )
    list_display_links = ( 'id' ,)
    #list_editable = (, , )
    #search_fields = ( , , )
    list_per_page = 20
admin.site.register( Booking , bookingAdmin)
admin.site.register( Exebition , exhibition)
admin.site.register( TimeSlot , timeslot)