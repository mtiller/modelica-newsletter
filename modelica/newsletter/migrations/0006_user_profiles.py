
from south.db import db
from django.db import models
from modelica.newsletter.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'UserProfile'
        db.create_table('newsletter_userprofile', (
            ('organization', models.CharField(max_length=200, blank=True)),
            ('id', models.AutoField(primary_key=True)),
            ('user', models.ForeignKey(orm['auth.User'], related_name='profile', unique=True)),
        ))
        db.send_create_signal('newsletter', ['UserProfile'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'UserProfile'
        db.delete_table('newsletter_userprofile')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'newsletter.newsletter': {
            'author': ('models.ForeignKey', ["'auth.User'"], {'verbose_name': '"Newsletter Author"', 'blank': 'True'}),
            'body': ('models.XMLField', [], {'blank': 'True'}),
            'footer': ('models.XMLField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'month': ('models.CharField', [], {'max_length': '20'}),
            'number': ('models.IntegerField', [], {}),
            'title': ('models.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'year': ('models.IntegerField', [], {})
        },
        'newsletter.section': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'issue': ('models.ForeignKey', ['Newsletter'], {}),
            'title': ('models.CharField', [], {'max_length': '100'}),
            'weight': ('models.IntegerField', [], {})
        },
        'newsletter.userprofile': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'organization': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('models.ForeignKey', ["'auth.User'"], {'related_name': "'profile'", 'unique': 'True'})
        },
        'newsletter.item': {
            'author': ('models.ForeignKey', ["'auth.User'"], {'verbose_name': '"Item Author"', 'blank': 'True'}),
            'body': ('models.XMLField', [], {}),
            'contributors': ('models.ManyToManyField', ["'auth.User'"], {'default': 'None', 'related_name': '"Contrbuting Authors"', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'upload_to': '"images"', 'blank': 'True'}),
            'org_url': ('models.URLField', [], {'blank': 'True'}),
            'organization': ('models.CharField', [], {'max_length': '200'}),
            'section': ('models.ForeignKey', ['Section'], {}),
            'title': ('models.CharField', [], {'max_length': '100'}),
            'weight': ('models.IntegerField', [], {})
        }
    }
    
    complete_apps = ['newsletter']
