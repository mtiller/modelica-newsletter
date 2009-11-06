from django.http import HttpResponse
from django.template import Context, loader
from modelica.newsletter.models import *

def index(request):
    return HttpResponse("Newsletter index")

def _dweight(s1,s2):
    return s1['obj'].weight-s2['obj'].weight;

def _iweight(i1,i2):
    return i1.weight-i2.weight;

def render(request, id):
    newsletter = Newsletter.objects.get(id=id)
    secobjs = Section.objects.filter(issue=newsletter)
    secs = []
    for obj in secobjs:
        items = []
        for item in Item.objects.filter(section=obj):
            items.append(item)
        items.sort(_iweight)
        secs.append({'obj': obj, 'items': items})
    secs.sort(_dweight)
    t = loader.get_template('render.html')
    c = Context({'issue': newsletter, 'secs': secs})
    return HttpResponse(t.render(c))

