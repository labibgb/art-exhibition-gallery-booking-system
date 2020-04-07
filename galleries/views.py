from django.shortcuts import render

def home( request ):
    return render( request , 'galleries/galleries.html')

def gallery( request ):
    return render( request , 'galleries/gallery.html')