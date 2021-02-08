import requests
import os
token=os.environ['token']
from pprint import pprint

#https://random.dog/5c9f8baf-7918-4545-bd86-8f441cf96f3e.jpg
def sendphoto(ids):
    url=f"https://api.telegram.org/bot{token}/sendPhoto"
    payload={
        'chat_id':ids,
        'photo':'https://random.dog/5c9f8baf-7918-4545-bd86-8f441cf96f3e.jpg',
        'caption':"title"
    }
    r=requests.get(url,params=payload)
    return r.json()
    
idx=937691492

pprint(sendphoto(idx))