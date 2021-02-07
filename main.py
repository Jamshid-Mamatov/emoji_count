import requests
import os
token=os.environ['token']

inform={}
like=0
dislike=0

def update():
    url=f"https://api.telegram.org/bot{token}/getUpdates"
    
    r=requests.get(url)
    
    data=r.json()
    message=data['result'][-1]['message']
    text=message.get('text')
    update_id=data['result'][-1]['update_id']
    from_id=data['result'][-1]['message']['from']['id']
    lst=[text,update_id,from_id]
    return lst

 
last_update_id=None
while True:

    lst=update()
    new_update_id=lst[1]
    
    if last_update_id!=new_update_id:
        last_update_id=new_update_id
        id=lst[2]
        text=lst[0]

        if inform.get(id)==None:
            inform[id]={'like':0,
                        'dislike':0
                        }
        elif text!=None:
            if text=='👎':
                dislike+=1
            elif text=="👍":
                like+=1
            
            inform[id]['like']=like
            inform[id]['dislike']=dislike

     
