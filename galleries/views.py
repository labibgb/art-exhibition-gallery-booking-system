from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Gallery
def home( request ):
    gallery = Gallery.objects.order_by('name').filter(is_published=True)
    paginator = Paginator( gallery , 6 )
    page = request.GET.get('page')
    pagr_gallerys = paginator.get_page(page)
    context = {
        'galleries' : pagr_gallerys
    }
    return render( request , 'galleries/galleries.html', context )

def gallery( request , gallery_id):
    gallery = Gallery.objects.order_by('name').filter(id=gallery_id)
    context = {
        'gallery' : gallery
    }
    return render( request , 'galleries/gallery.html' , context)