from django.urls import path, include

from .views import dgouiform,mymapsform,mymapsdrawform

urlpatterns = [
    path('', dgouiform, name='default'),
    path('mymaps/',mymapsform,name='mymaps'),
    path('mymaps/draw/',mymapsdrawform,name="drawmaps")
    
]