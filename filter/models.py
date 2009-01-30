### these models are for testing

from django.db import models

STATUS_CHOICES = (
    (0, 'Regular'),
    (1, 'Admin'),
)

class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    
    is_active = models.BooleanField()
    
    favorite_books = models.ManyToManyField('Book')
    
    def __unicode__(self):
        return self.username

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User)
    
    date = models.DateField()
    
    def __unicode__(self):
        return "%s said %s" % (self.author, self.text[:25])

class Book(models.Model):
    title = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.title
