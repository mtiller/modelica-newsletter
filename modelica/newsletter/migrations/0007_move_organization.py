
from south.db import db
from django.db import models
from modelica.newsletter.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'UserProfile.org_url'
        db.add_column('newsletter_userprofile', 'org_url', models.URLField(blank=True, null=True))
    
    def backwards(self, orm):
        
        # Deleting field 'UserProfile.org_url'
        db.delete_column('newsletter_userprofile', 'org_url')
        
        # Adding field 'Item.org_url'
        db.add_column('newsletter_item', 'org_url', models.URLField(blank=True))
        
        # Adding field 'Item.organization'
        db.add_column('newsletter_item', 'organization', models.CharField(max_length=200))
        
    
    
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
            'org_url': ('models.URLField', [], {'blank': 'True'}),
            'organization': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('models.ForeignKey', ["'auth.User'"], {'related_name': "'profile'", 'unique': 'True'})
        },
        'newsletter.item': {
            'author': ('models.ForeignKey', ["'auth.User'"], {'verbose_name': '"Item Author"', 'blank': 'True'}),
            'body': ('models.XMLField', [], {}),
            'contributors': ('models.ManyToManyField', ["'auth.User'"], {'default': 'None', 'related_name': '"Contrbuting Authors"', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'upload_to': '"images"', 'blank': 'True'}),
            'section': ('models.ForeignKey', ['Section'], {}),
            'title': ('models.CharField', [], {'max_length': '100'}),
            'weight': ('models.IntegerField', [], {})
        }
    }
    
    complete_apps = ['newsletter']
