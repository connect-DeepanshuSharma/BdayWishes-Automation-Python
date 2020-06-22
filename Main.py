#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
import time
from twilio.rest import Client

def sendMsg(to,msg,number):
    print(f"Msg send to {to} which is {msg} on {number}")
    account_sid = 'YOUR TWILIO ID HERE' 
    auth_token = 'YOUR TOKEN HERE' 
    client = Client(account_sid, auth_token) 

    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body=msg,      
                                  to=f'whatsapp:+91{number}' 
                              ) 
    
    
        
if __name__=="__main__":
    time.sleep(10)
    df=pd.read_excel("Bday.xlsx")
    # %d for date extraction %m for month and %Y for year extraction
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%Y")
    writeInd=[]
    for index,item in df.iterrows():
        bday=item["Birthday"].strftime("%d-%m")
        if(bday==today and yearNow not in str(item['Year'])):
            sendMsg(item["Name"] ,item["Dialog"],item["Number"])
            writeInd.append(index)
    for i in writeInd:
        yr=df.loc[i,'Year']
        df.loc[i,'Year']=str(yr)+','+str(yearNow)
        df.to_excel('Bday.xlsx', index=False)
        

  



# In[ ]:




