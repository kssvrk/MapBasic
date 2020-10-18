from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def dgouiform(request):
    template = loader.get_template('dgoui/form.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))