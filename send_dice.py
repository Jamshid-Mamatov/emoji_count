import requests
import os
token=os.environ['token']
from pprint import pprint

def sendDice(ids):
    url=f"https://api.telegram.org/bot{token}/sendDice"
    

    payload={
        'chat_id':ids,
        'emoji':["🎲","🎰", "🎯", "🏀", "⚽"]
    }
    r=requests.get(url,params=payload)
    return r.json()
    
idx=937691492

pprint(sendDice(idx))
