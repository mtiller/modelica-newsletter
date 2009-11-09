from django.db import models

class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', unique=True, related_name='profile')
    organization = models.CharField(max_length=200, blank=True)
    org_url = models.URLField(blank=True)
    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class Newsletter(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    number = models.IntegerField()
    footer = models.XMLField(null=True,blank=True)

    author = models.ForeignKey('auth.User', verbose_name="Newsletter Author",
                               blank=True)
    title = models.CharField(max_length=100,blank=True)
    body = models.XMLField(blank=True)

    def __unicode__(self):
        return "%d-%d (%s)" % (self.year, self.number, self.month)

class Section(models.Model):
    title = models.CharField(max_length=100)
    issue = models.ForeignKey(Newsletter)
    weight = models.IntegerField()
    def __unicode__(self):
        return "%s [%s]" % (self.title, unicode(self.issue))

# Create your models here.
class Item(models.Model):
    author = models.ForeignKey('auth.User', verbose_name="Item Author",
                               blank=True)
    image = models.ImageField(upload_to="images",blank=True)
    title = models.CharField(max_length=100)
    body = models.XMLField()
    section = models.ForeignKey(Section)
    weight = models.IntegerField()
    contributors = models.ManyToManyField('auth.User', related_name="Contrbuting Authors", default=None, blank=True)
    def __unicode__(self):
        return "%s: '%s' %s" % (unicode(self.author), unicode(self.title), unicode(self.section))
