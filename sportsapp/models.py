
#from django.db.models.fields import DateField
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.db.models.manager import GeoManager
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender_choices = (('M','Male'),
                        ('F','Female'),
                        ('O','Others'))
    user_gender = models.CharField(choices = gender_choices,max_length=1,blank=True)
    #dob = models.DateField()
    last_location = models.PointField(max_length=40, blank=True,spatial_index=True, geography=True)
    prefered_radius = models.IntegerField(default=5, help_text="in kilometers")
    objects = GeoManager()
