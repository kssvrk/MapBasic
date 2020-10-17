#from django.db import models
from django.contrib.gis.db import models


# Create your models here.

class LocationUser(models.Model):
    #telegram_id = models.CharField(max_length=100,unique=True)
    telegram_username=models.CharField(max_length=1000,unique=True)
    locuser_id = models.AutoField(primary_key=True)
    enable = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)
    text_sent=models.CharField(max_length=1000,null=True,blank=True)

    def __str__(self):
        return f"{self.telegram_username} with id {self.locuser_id}"


class LocationStream(models.Model):
    locuser=models.ForeignKey(LocationUser,on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField(auto_now_add=True)
    location = models.PointField()

    def __str__(self):
        return f"{self.locuser} with id {self.location}"





