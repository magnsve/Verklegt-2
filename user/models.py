from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=9999)

    def __str__(self):
        return self.name


class UserImage(models.Model):
    image = models.CharField(max_length=9999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)