from django.contrib import admin
from .models import Gallery, Location,ServiceList, Services, Feedback
class galleyAdmin( admin.ModelAdmin ):
    list_display = ( 'id' , 'name', 'rent_per_day', 'location' , 'is_available' , 'is_published' )
    list_display_links = ( 'id', 'name', )
    list_filter = ( 'is_published' , 'location' , 'is_available')
    list_editable = ( 'location' , 'rent_per_day','is_available' , 'is_published' )
    list_per_page = 20

admin.site.register( Gallery , galleyAdmin )
admin.site.register( Location )
admin.site.register( ServiceList )
admin.site.register( Services )
admin.site.register( Feedback )
