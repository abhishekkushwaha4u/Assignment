from django.db import models
# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    dob = models.DateField()

    def __str__(self):
        return self.name
     
class Book(models.Model):
    name = models.CharField(max_length = 100)
    published = models.DateField()
    author = models.ForeignKey(Author,on_delete = models.CASCADE)

    def __str__(self):
        return self.name+" "+self.author.name





