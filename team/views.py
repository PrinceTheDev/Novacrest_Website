from django.http import HttpResponse
from django.template import loader


def team(request):
    template = loader.get_template('team/team.html')
    return HttpResponse(template.render({}, request))