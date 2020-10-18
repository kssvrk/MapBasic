from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from django.conf import settings
def corecontext(dict):
    dict['site_brand_name']=settings.SITE_BRAND_NAME
    return dict
def dgouiform(request):
    template = loader.get_template('dgoui/form.html')
    context = {
        
    }
    context=corecontext(context)
    return HttpResponse(template.render(context, request))