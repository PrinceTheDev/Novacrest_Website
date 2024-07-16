from django.shortcuts import render

def gallery(request):
    context = {
        'images': [
            'image1.jpg',
            'image2.jpg',
            'image3.jpg',
        ],
    }
    return render(request, 'gallery/gallery.html', context)
