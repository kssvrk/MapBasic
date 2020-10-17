from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import json
from django.views.decorators.csrf import csrf_exempt
from .models import LocationStream,LocationUser
from django.contrib.gis.geos import  Point
from datetime import datetime
from .telegram_bot import sendTBotMessage


def process_new_user_telegram(user_name):
    locuser=LocationUser(telegram_username=user_name)
    locuser.save()
def update_location(msg,user_name):
    if('location' in msg.keys()):
        latitude=msg['location']['latitude']
        longitude=msg['location']['longitude']
        pnt = Point(longitude, latitude, srid=4326)
        locuser=LocationUser.objects.get(telegram_username=user_name)
        print(pnt)
        streams=LocationStream.objects.filter(locuser=locuser)
        if(len(streams)>0):
            stream=streams[0]
            stream.location=pnt 
            stream.save()
        else:
            stream=LocationStream(locuser=locuser,location=pnt)
            stream.save()
        

@csrf_exempt 
def bot(request):
    if request.method == 'POST':
        print(request.body.decode('utf-8'))
        json_data = json.loads(request.body.decode('utf-8')) # request.raw_post_data w/ Django < 1.4
        
        try:
            message_key=''
            if('message' in json_data.keys()):
                message_key='message'
            elif('edited_message' in json_data.keys()):
                message_key='edited_message'
            if(message_key==''):
                #-------------------------------
                text='Wrong Message Key comezz'
                #-------------------------------
                return JsonResponse({'response':'very good telegram'},status=200)
            user_name=json_data[message_key]['from']['username']
            msg_id=json_data[message_key]['message_id']
            chat_id=json_data[message_key]['chat']['id']
            locuser=LocationUser.objects.filter(telegram_username=user_name)
            if(len(locuser)==0):
                #process_new_user
                process_new_user_telegram(user_name)
                #-------------------------------
                text=f'Created a new User for bot services {user_name}'
                print(text)
                sendTBotMessage(chat_id,text,reply_to_msg_id="")
                #-------------------------------
            #process_existing_user
            if(locuser[0].enable==True):
                msg=json_data[message_key]
                update_location(msg,user_name)
                return JsonResponse({'response':'very good telegram'},status=200)
            else:
                print('User is not enabled for bot services')
                #-------------------------------
                text=f'{user_name} is not yet Enabled by admin for Bot services. Contact 9398106836'
                print(text)
                sendTBotMessage(chat_id,text,reply_to_msg_id=msg_id)
                #-------------------------------
                return JsonResponse({'response':'very good telegram'},status=200)

            
            return JsonResponse({'response':'very good telegram'},status=200)
        except Exception as e:
            #-------------------------------
                text='Did not find any message with the update , Key error , Unstructured data'
                print(text+str(e))
                sendTBotMessage(chat_id,text,reply_to_msg_id=msg_id)
                #-------------------------------
                return JsonResponse({'response':'very good telegram'},status=200)
    else:
        #-------------------------------
                text='Non standard request method by telegram'
                print(text)
                sendTBotMessage(chat_id,text,reply_to_msg_id=msg_id)
                #-------------------------------
                return JsonResponse({'response':'very good telegram'},status=200)
        
