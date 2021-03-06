from django.db import models
# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.id+" "+self.name
     
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    published = models.DateField()
    author = models.ForeignKey(Author,related_name="book",on_delete = models.CASCADE)

    def __str__(self):
        return self.id+" "+self.name






