from django.db import models
from django.contrib.auth.models import User
import datetime as dt



class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profiles/', null=True)
    bio = models.TextField( null=True)
    user = models.ForeignKey(User)

    def __str__(self):
        '''
        Display for profiles in profile table
        '''
        return self.user.username

# Create your models here v.
class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User)


class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    image_name = models.CharField(max_length=30)
    image_caption =models.TextField(max_length = 30, null =True,blank=True)
    likes = models.IntegerField()
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    comments = models.ManyToManyField(Comments)
    user = models.ForeignKey(User)

    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()

    @classmethod
    def get_images(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            gotten_image_posts : list of image post objects from the database
        '''
        gotten_images = Image.objects.all()
        return gotten_images
