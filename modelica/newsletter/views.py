from django.http import HttpResponse
from django.template import Context, loader
from modelica.newsletter.models import *

def index(request):
    return HttpResponse("Newsletter index")

def _dweight(s1,s2):
    return s1['obj'].weight-s2['obj'].weight;

def _iweight(i1,i2):
    return i1.weight-i2.weight;

def _info(id):
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
    return (newsletter, secs)

def render(request, id):
    (newsletter, secs) = _info(id)
    t = loader.get_template('render.html')
    c = Context({'issue': newsletter, 'secs': secs})
    return HttpResponse(t.render(c))

def email(request, id):
    (newsletter, secs) = _info(id)
    t = loader.get_template('email.html')
    c = Context({'issue': newsletter,
                 'urlroot': 'publications/newsletters',
                 'bordercolor': 'black',
                 'titlebg': '#c9141a',
                 'headingbg': '#B0B0B0',
                 'itembg': '#E8E8E8',
                 'secs': secs})
    return HttpResponse(t.render(c))

def upload_ftp(request, id):
    from ftplib import FTP
    if request.method == 'POST':
        form = CredentialsForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            (newsletter, secs) = _info(id)
            t = loader.get_template('render.html')
            c = Context({'issue': newsletter, 'secs': secs})
            txt = t.render(c)
            ftp = FTP('localhost', 10021, username, password)
            ftp.login()
            cwd = "/publications/newsletter/%d-%d" % (newsletter.year,
                                                      newsletter.number)
            ftp.cwd(cwd)
            return HttpResponse("Uploading %s!" % (id,))
    else:
        form = CredentialsForm()

    return render_to_response("credentials.html",
                              {"form": form,
                               "action": "/newsletter/%s/upload" % (id,)})

def upload_fs(request, id):
    import modelica.newsletter
    import os
    import shutil
    (newsletter, secs) = _info(id)
    t = loader.get_template('render.html')
    c = Context({'issue': newsletter, 'secs': secs})
    txt = t.render(c).encode("utf-8")
    tdir = os.path.join(str(modelica.newsletter.__path__[0]),
                        "publish",
                        "%4d-%d" % (newsletter.year, newsletter.number))
    idir = os.path.join(tdir, "images")
    if not os.path.exists(tdir):
        os.mkdir(tdir)
    if not os.path.exists(idir):
        os.mkdir(idir)
    out = os.path.join(tdir,"index_html")
    f = open(out, "w+")
    print >> f, txt
    f.close()
    for sec in secs:
        for item in sec["items"]:
            src = item.image.file.name
            dst = os.path.join(idir, os.path.basename(src))
            shutil.copyfile(src, dst)
    return HttpResponse("Files written in "+tdir)
