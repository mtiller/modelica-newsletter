
from south.db import db
from django.db import models
from modelica.newsletter.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Deleting field 'Newsletter.author_email'
        # db.delete_column('newsletter_newsletter', 'author_email')
        
        # Deleting field 'Item.author_email'
        # db.delete_column('newsletter_item', 'author_email')
        
        # Deleting field 'Item.author'
        # db.delete_column('newsletter_item', 'author')
        
        # Deleting field 'Newsletter.author'
        # db.delete_column('newsletter_newsletter', 'author')
        pass

    def backwards(self, orm):
        
        # Adding field 'Newsletter.author_email'
        db.add_column('newsletter_newsletter', 'author_email', models.EmailField(blank=True))
        
        # Adding field 'Item.author_email'
        db.add_column('newsletter_item', 'author_email', models.EmailField(blank=True))
        
        # Adding field 'Item.author'
        db.add_column('newsletter_item', 'author', models.CharField(max_length=200))
        
        # Adding field 'Newsletter.author'
        db.add_column('newsletter_newsletter', 'author', models.CharField(max_length=200, blank=True))
        
    
    
    models = {
        'newsletter.newsletter': {
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
