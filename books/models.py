from django.db import models

# Create your models here.
class User (models.Model):
    username = models.CharField(max_length=128, unique=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    no_reviews = models.IntegerField(default=0)
    url = models.URLField(unique=True)
    books = models.CharField(max_length=500)

    def __str__(self):
        return self.username

class Book (models.Model):
    title = models.CharField(max_length=128, unique=True)
    year = models.IntegerField(default=2021)
    publisher = models.CharField(max_length=128)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    url = models.URLField(unique=True)
    cover = models.ImageField(upload_to='covers', blank=True)
    authors = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



class Review(models.Model):
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=1000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)

class Author(models.Model):
    name = models.CharField(max_length=128)
    books = models.ManyToManyField(Book)
