import requests
import os
token=os.environ['token']

inform={}
inform['like']=0
inform['dislike']=0
def update():
    url=f"https://api.telegram.org/bot{token}/getUpdates"
    
    r=requests.get(url)
    like=0
    dislike=0
    data=r.json()
    text=data['result'][-1]['message']['text']
                
    if text=='👎':
        dislike+=1
    elif text=="👍":
        like+=1

    inform['like']=like
    inform['dislike']=dislike


def update_id():
    url=f"https://api.telegram.org/bot{token}/getUpdates"
    
    r=requests.get(url)
    data=r.json()
    id=data['result'][-1]['update_id']
    return id

    
last_update_id=None
while True:

    new_update_id=update_id()
    if last_update_id!=new_update_id:
        update()
