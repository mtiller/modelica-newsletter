from django.http import HttpResponse
from django.template import Context, loader
from modelica.newsletter.models import *

def index(request):
    return HttpResponse("Newsletter index")

def render(request, id):
    newsletter = Newsletter.objects.get(id=id)
    secobjs = Section.objects.filter(issue=newsletter)
    secs = []
    for obj in secobjs:
        secs.append({'obj': obj, 'items': Item.objects.filter(section=obj)})
    t = loader.get_template('render.html')
    c = Context({'issue': newsletter, 'secs': secs})
    return HttpResponse(t.render(c))

