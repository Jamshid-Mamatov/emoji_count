import requests
import os
token=os.environ['token']
from pprint import pprint

#https://random.dog/5c9f8baf-7918-4545-bd86-8f441cf96f3e.jpg
def sendDoc(ids):
    url=f"https://api.telegram.org/bot{token}/sendDocument"
    document=open("readme.md",'rb')

    payload={
        'chat_id':ids,
        
        'caption':"title"
    }
    r=requests.get(url,params=payload,files={'document':document})
    return r.json()
    
idx=937691492

pprint(sendDoc(idx))