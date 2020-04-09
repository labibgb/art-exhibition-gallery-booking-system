from django.shortcuts import render
from galleries.models import Gallery
def home( request ):
    gallery = Gallery.objects.order_by('name').filter(is_published=True).filter(is_available=True)[:3]
    context = {
        'galleries' : gallery
    }
    return render( request , 'pages/index.html', context )

def about( request ):
    return render( request , 'pages/about.html')
