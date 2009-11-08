
from south.db import db
from django.db import models
from modelica.newsletter.models import *
from django.contrib.auth.models import User, Group

class Migration:
    
    def forwards(self, orm):
        
        # Adding ManyToManyField 'Item.contributors'
        db.create_table('newsletter_item_contributors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(Item, null=False)),
            ('user', models.ForeignKey(User, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Dropping ManyToManyField 'Item.contributors'
        db.delete_table('newsletter_item_contributors')
        
    
    
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
