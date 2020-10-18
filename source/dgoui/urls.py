from django.urls import path, include

from .views import dgouiform

urlpatterns = [
    path('dgoui', dgouiform, name='default'),
    
]