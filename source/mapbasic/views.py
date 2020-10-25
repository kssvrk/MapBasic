from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from django.conf import settings
from django.core.paginator import Paginator
from .models import UserMap
from django.contrib.auth.decorators import login_required
import math
from .forms import UserMapForm
from django.shortcuts import get_object_or_404

def corecontext(dict):
    dict['site_brand_name']=settings.SITE_BRAND_NAME
    return dict
def dgouiform(request):
    template = loader.get_template('mapbasic/index.html')
    context = {
        
    }
    context=corecontext(context)
    return HttpResponse(template.render(context, request))
@login_required
def mymapsform(request):
    #use paginator to show the maps of the users.
    map_list= UserMap.objects.filter(user=request.user)
    paginate_value=7
    map_paginator = Paginator(map_list, paginate_value) 

    page_number = request.GET.get('page',1)
    page_obj = map_paginator.get_page(page_number)
    client_maps=[]
    for user_map in page_obj:
        client_maps.append(
            {
                "name":user_map.name,
                "description":user_map.description,
                "updated_at":user_map.updated_at,
                "id":user_map.id
            }
        )
    template = loader.get_template('mapbasic/mymaps/view.html')
    context = {
        "map_list":client_maps,
        "next_page":int(page_number)+1,
        "previous_page":int(page_number)-1,
        "page_number":int(page_number),
        "max_pages":math.ceil(map_paginator.count/paginate_value)
    }
    #print(map_list)
    context=corecontext(context)
    return HttpResponse(template.render(context, request))
@login_required
def mymapsdrawform(request):
    # if this is a POST request we need to process the form data
    context={}
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        usermapform = UserMapForm(request.POST)
        if(usermapform.is_valid()):
            map_obj=usermapform.cleaned_data
            print(map_obj)
            try:
                
                mapmodel=UserMap(name=map_obj['name'],description=map_obj['description'],aoi=map_obj['aoi'],user_id=request.user.id)
                mapmodel.save()
                context['save_status']='done'
                context['usermapform']=UserMapForm()
            except Exception as e:
                context['save_status']='error'
                context['errors']='Error while saving the user map'
                print(e)
                context['usermapform']=usermapform
            
        else:
            context['save_status']='error'
            context['errors']=usermapform.errors
            context['usermapform']=usermapform
        context=corecontext(context)
        template = loader.get_template('mapbasic/mymaps/createmap.html')
        return HttpResponse(template.render(context, request))
    else:
        context['save_status']='0'
        mymapid = request.GET.get('mymapid',"none")
        if(str(mymapid)=='none'):
            context['usermapform']=UserMapForm()
        else:
            map_obj= get_object_or_404(UserMap,id=mymapid)
            populate={
                'name':map_obj.name,
                'description':map_obj.description,
                'aoi':map_obj.aoi
            }
            
            context['usermapform']=UserMapForm(initial=populate)
        
    template = loader.get_template('mapbasic/mymaps/createmap.html')
    
    
    context=corecontext(context)
    return HttpResponse(template.render(context, request))