from django.contrib.gis import admin
# from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.
from .models import LocationUser,LocationStream

admin.site.register(LocationStream)
admin.site.register(LocationUser)