
from south.db import db
from django.db import models
from modelica.newsletter.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Item.weight'
        db.add_column('newsletter_item', 'weight', models.IntegerField(default=0), keep_default=False)
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Item.weight'
        db.delete_column('newsletter_item', 'weight')
        
    
    
    models = {
        'newsletter.newsletter': {
            'author': ('models.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'author_email': ('models.EmailField', [], {'blank': 'True'}),
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
            'author': ('models.CharField', [], {'max_length': '200'}),
            'author_email': ('models.EmailField', [], {'blank': 'True'}),
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
