from django.http import HttpResponse
from django.template import loader


def contact(request):
    template = loader.get_template('contact/contact.html')
    return HttpResponse(template.render()) 