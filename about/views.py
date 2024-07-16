from django.shortcuts import render

def about_us(request):
    context = {
        'hospital_name': "Novacrest Hospital",
        'about_text': "Novacrest Hospital is a leading mental health faclity....",
    }
    return render(request, 'about/about_us.html', context)
