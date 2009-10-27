from django.db import models

class Newsletter(models.Model):
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    number = models.IntegerField()
    footer = models.XMLField(null=True,blank=True)

    author = models.CharField(max_length=200,blank=True)
    author_email = models.EmailField(blank=True)
    title = models.CharField(max_length=100,blank=True)
    body = models.XMLField(blank=True)

    def __str__(self):
        return "%d-%d (%s)" % (self.year, self.number, self.month)

class Section(models.Model):
    title = models.CharField(max_length=100)
    issue = models.ForeignKey(Newsletter)
    weight = models.IntegerField()
    def __str__(self):
        return "%s [%s]" % (self.title, str(self.issue))

# Create your models here.
class Item(models.Model):
    author = models.CharField(max_length=200)
    author_email = models.EmailField(blank=True)
    image = models.ImageField(upload_to="images",blank=True)
    organization = models.CharField(max_length=200)
    org_url = models.URLField(blank=True)
    title = models.CharField(max_length=100)
    body = models.XMLField()
    section = models.ForeignKey(Section)
    def __str__(self):
        return "%s %s" % (self.author, str(self.section))
