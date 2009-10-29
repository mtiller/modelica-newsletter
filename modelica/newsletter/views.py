from django.http import HttpResponse
from django.template import Context, loader
from modelica.newsletter.models import *

def index(request):
    return HttpResponse("Newsletter index")

def _dweight(s1,s2):
    return s1['obj'].weight-s2['obj'].weight;

def render(request, id):
    newsletter = Newsletter.objects.get(id=id)
    secobjs = Section.objects.filter(issue=newsletter)
    secs = []
    for obj in secobjs:
        secs.append({'obj': obj, 'items': Item.objects.filter(section=obj)})
    secs.sort(_dweight)
    t = loader.get_template('render.html')
    c = Context({'issue': newsletter, 'secs': secs})
    return HttpResponse(t.render(c))

