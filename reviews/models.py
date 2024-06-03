from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Review(models.Model):
    email   = models.EmailField()
    comment = models.TextField()
    rating  = models.IntegerField(default=0)
    likes   = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    


    def __str__(self) -> str:
        return self.email
    

