# Create your models here.
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class UserMap(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=5000)
    aoi = models.PolygonField(srid=4326)
    added_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)