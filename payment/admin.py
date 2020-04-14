from django.contrib import admin
from .models import Payment
# Register your models here.

class payment( admin.ModelAdmin ):

    list_display = ( 'id' , 'user', 'booking' , 'total_pay' , 'is_payment' )
    list_display_links = ( 'id', 'user', )
    list_filter = ( 'is_payment' ,)
    list_per_page = 20     


admin.site.register( Payment, payment )