from django.shortcuts import render

def services(request):
    context = {
        'services': [
            'In-patient Treatment',
            'Out-patient Treatment',
            'Rehabilitation Services',
            'Counselling and Therapy',
            'Medication Management',
        ],
    }
    return render(request, 'services/services.html', context)
