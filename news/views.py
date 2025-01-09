from django.http import HttpResponse
from django.template import loader


def news(request):
    template = loader.get_template('news/news.html')
    return HttpResponse(template.render())