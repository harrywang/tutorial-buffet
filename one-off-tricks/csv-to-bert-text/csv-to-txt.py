#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import os
import shutil


# In[20]:


sent = pd.read_csv("real.csv", encoding='utf8')
sent


# In[21]:


path = os.getcwd()
print ("The current working directory is %s" % path)


# In[32]:


# clean data folder and create new folders
shutil.rmtree('./data')
os.makedirs("./data/pos")
os.makedirs("./data/neg")
os.makedirs("./data/neu")


# In[16]:


def write_sent(label, id, sent):
    filename = "./data/"+ label +"/" + id +".txt"
    file = open(filename,"w")
    file.writelines(sent)
    file.close()


# In[17]:


for index, row in sent.iterrows():
    write_sent(row['SentiLabel_food'].lower(), str(row['SentenceID']), row['Sentences'])
    print("writing sentence")
