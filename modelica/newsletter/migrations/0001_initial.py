
from south.db import db
from django.db import models
from modelica.newsletter.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Newsletter'
        db.create_table('newsletter_newsletter', (
            ('body', models.XMLField(blank=True)),
            ('footer', models.XMLField(null=True, blank=True)),
            ('author_email', models.EmailField(blank=True)),
            ('author', models.CharField(max_length=200, blank=True)),
            ('number', models.IntegerField()),
            ('month', models.CharField(max_length=20)),
            ('year', models.IntegerField()),
            ('title', models.CharField(max_length=100, blank=True)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('newsletter', ['Newsletter'])
        
        # Adding model 'Section'
        db.create_table('newsletter_section', (
            ('issue', models.ForeignKey(orm.Newsletter)),
            ('id', models.AutoField(primary_key=True)),
            ('weight', models.IntegerField()),
            ('title', models.CharField(max_length=100)),
        ))
        db.send_create_signal('newsletter', ['Section'])
        
        # Adding model 'Item'
        db.create_table('newsletter_item', (
            ('body', models.XMLField()),
            ('author', models.CharField(max_length=200)),
            ('author_email', models.EmailField(blank=True)),
            ('title', models.CharField(max_length=100)),
            ('image', models.ImageField(upload_to="images", blank=True)),
            ('org_url', models.URLField(blank=True)),
            ('section', models.ForeignKey(orm.Section)),
            ('organization', models.CharField(max_length=200)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('newsletter', ['Item'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Newsletter'
        db.delete_table('newsletter_newsletter')
        
        # Deleting model 'Section'
        db.delete_table('newsletter_section')
        
        # Deleting model 'Item'
        db.delete_table('newsletter_item')
        
    
    
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
            'title': ('models.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['newsletter']
