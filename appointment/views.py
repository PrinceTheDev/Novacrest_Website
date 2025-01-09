from django.http import HttpResponse
from django.template import loader

def appointment(request):
    template = loader.get_template('appointment/appointment.html')
    return HttpResponse(template.render())