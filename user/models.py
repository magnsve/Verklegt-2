from django.contrib.auth.models import User
from django.db import models


#Main class for user profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=9999)
    profile_image = models.CharField(max_length=9999)
    admin = models.BooleanField(default=False)


#Main class for Search history, it has to be tied to a user
class SearchHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    search_string = models.CharField(max_length=255)
    timestamp = models.DateField(auto_now=True)
