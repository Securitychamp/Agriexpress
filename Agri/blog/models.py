from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    content2 = models.TextField()
    content3 = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/')
    featured_image1 = models.ImageField(upload_to='post_images/')
    featured_image2 = models.ImageField(upload_to='post_images/')
    featured_image3 = models.ImageField(upload_to='post_images/')
    def __str__(self):
        return self.title




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_pictures/')

    def __str__(self):
        return self.user.username





from django.db import models

# Create your models here.
