from django.contrib.gis import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import UserMap

@admin.register(UserMap)
class UserMapAdmin(OSMGeoAdmin):
    list_display = ('name', 'description','aoi','user','updated_at','added_at')