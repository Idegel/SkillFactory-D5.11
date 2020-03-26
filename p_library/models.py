from django.db import models

# Create your models here.
from django.db import models  

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)

    def __str__(self):  
        return "{},{}".format(self.full_name,self.birth_year)

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    editor = models.ForeignKey('Editor', on_delete=models.CASCADE,null=True,blank=True,related_name='books')
    friend = models.ForeignKey('Friend', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title

class Editor(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Friend(models.Model):
    full_name = models.TextField()
    
    def __str__(self):
        return self.full_name
