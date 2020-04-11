from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallery
from booking.models import Exebition, TimeSlot
def home( request ):
    gallery = Gallery.objects.order_by('name').filter(is_published=True)
    paginator = Paginator( gallery , 6 )
    page = request.GET.get('page')
    pagr_gallerys = paginator.get_page(page)
    exhibition = Exebition.objects.order_by('id').all()
    timeslot = TimeSlot.objects.order_by('id').all()
    context = {
        'galleries' : pagr_gallerys,
        'exebition' : exhibition,
        'timeslot' : timeslot
    }
    return render( request , 'galleries/galleries.html', context )

def gallery( request , gallery_id):
    gallery = Gallery.objects.order_by('name').filter(id=gallery_id)
    exhibition = Exebition.objects.order_by('id').all()
    timeslot = TimeSlot.objects.order_by('id').all()
    context = {
        'gallery' : gallery,
        'exebition' : exhibition,
        'timeslot' : timeslot
    }
    return render( request , 'galleries/gallery.html' , context)