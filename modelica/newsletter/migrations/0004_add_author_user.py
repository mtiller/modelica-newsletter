
from south.db import db
from django.db import models
from modelica.newsletter.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Item.author'
        db.add_column('newsletter_item', 'author', models.ForeignKey(orm['auth.User'], verbose_name="Item Author", blank=True, null=True))
        
        # Adding field 'Newsletter.author'
        db.add_column('newsletter_newsletter', 'author', models.ForeignKey(orm['auth.User'], verbose_name="Newsletter Author", blank=True, null=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Item.author'
        db.delete_column('newsletter_item', 'author_id')
        
        # Deleting field 'Newsletter.author'
        db.delete_column('newsletter_newsletter', 'author_id')
        
    
    
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
        'newsletter.item': {
            'author': ('models.ForeignKey', ["'auth.User'"], {'verbose_name': '"Item Author"', 'blank': 'True'}),
            'body': ('models.XMLField', [], {}),
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
