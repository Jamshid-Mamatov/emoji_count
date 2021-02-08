import requests
import os
token=os.environ['token']
from pprint import pprint

#https://random.dog/5c9f8baf-7918-4545-bd86-8f441cf96f3e.jpg
def sendphoto(ids):
    url=f"https://api.telegram.org/bot{token}/sendPhoto"
    photo=open("logo.jpg",'rb')

    payload={
        'chat_id':ids,
        
        'caption':"send phot file_id"
    }
    r=requests.get(url,params=payload,files={'photo':photo})
    return r.json()
    
idx=937691492

pprint(sendphoto(idx))