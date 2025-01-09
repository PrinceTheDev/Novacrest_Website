from django.http import HttpResponse
from django.template import loader


def services(request):
    template = loader.get_template('services/services.html')
    return HttpResponse(template.render({}, request))
