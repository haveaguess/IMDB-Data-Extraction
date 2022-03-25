#!/usr/bin/env python
# coding: utf-8

# # Film (BOM)
# 
# 
# ### Aggregate Box Office Numbers per Title

# In[14]:


import requests
import lxml.html as lh
import pandas as pd
year = ['2016','2017','2018','2019','2020']

for y in year :
    url='https://www.boxofficemojo.com/year/world/'+y
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    col=[]
    i=0
    for t in tr_elements[0]:
        i+=1
        name=t.text_content()
        col.append((name,[]))
    for j in range(1,len(tr_elements)):
        T=tr_elements[j]
        if len(T)!=7:
            break
        i=0
        for t in T.iterchildren():
            data=t.text_content() 
            if i>0:
                try:
                    data=int(data)
                except:
                    pass
            col[i][1].append(data)
            i+=1
    Dict={title:column for (title,column) in col}      
    if   y == '2020':
        dfOne=pd.DataFrame(Dict).assign(Year=y)
    elif y == '2019':
        dfTwo=pd.DataFrame(Dict).assign(Year=y)
    elif y == '2018':
        dfThree=pd.DataFrame(Dict).assign(Year=y)
    elif y == '2017':
        dfFour=pd.DataFrame(Dict).assign(Year=y)
    elif y == '2016':
        dfFive=pd.DataFrame(Dict).assign(Year=y)        
Aggregate = pd.concat([dfOne,dfTwo,dfThree,dfFour,dfFive], ignore_index=True)  
Aggregate.columns = Aggregate.columns.str.replace(' ', '')
Aggregate = Aggregate.rename(columns={"Rank": "Number", "ReleaseGroup\n": "Title","%":"Change"})
Aggregate = Aggregate.set_index(['Title'])
Film = Aggregate.drop(['Number'],axis =1)
Film


# In[19]:


Film.sample(7)


# In[15]:


Film.shape


# In[16]:


Film.info()


# In[17]:


Film.describe()


# # Notes 
# ### 1. Numbers have 10-20% Error compare with IBOE
# 
