import requests
import os
token=os.environ['token']
from pprint import pprint

#https://random.dog/5c9f8baf-7918-4545-bd86-8f441cf96f3e.jpg
def sendContact(ids):
    url=f"https://api.telegram.org/bot{token}/sendContact"
    

    payload={
        'chat_id':ids,
        'phone_number':123456789,
        'first_name':'Jamshid'
        
    }
    r=requests.get(url,params=payload)
    return r.json()
    
idx=937691492

pprint(sendContact(idx))