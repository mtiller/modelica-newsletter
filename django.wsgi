import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'modelica.settings'
sys.path.append('/home/django/modelica-newsletter/modelica')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
