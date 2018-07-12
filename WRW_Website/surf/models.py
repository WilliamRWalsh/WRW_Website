from django.db import models


class Author(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)

    def __str__(self):
        return "%s %s" % (self.firstName, self.lastName)

    def __unicode__(self):
        return "%s %s" % (self.firstName, self.lastName)



class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

