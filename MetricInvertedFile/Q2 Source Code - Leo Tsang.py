#!/usr/bin/env python
# coding: utf-8

# #Create a MIF File
# 

# In[3]:


import numpy as np
from numpy import genfromtxt


# In[4]:


my_data = genfromtxt('Q1_LEO_TSANG.csv', delimiter=',')


# In[5]:


#taking 1000 rows to be my reference point
reference = my_data[np.random.choice(len(my_data),1000,replace=True)]


# In[11]:


def distance(x,y):
  return(abs(x-y))


# In[10]:


#here i am calculating the distance and summing it sorting the index of it
dist_l = []
dist_l_filter = []
dist_filter = []

for i in my_data:
  for j in reference:
    
    dist_filter.append(np.sum((distance(i[1],j[1]))))

    if len(dist_filter) == len(reference):
      dist_filter = np.array(dist_filter)
      filterd = np.argsort(dist_filter)[:10]
      dist_l_filter.extend(filterd)
      dist_filter = []
      dist_filter.clear()


# In[12]:


#pruned order_list
pruned_ordered_list = np.reshape(np.asarray(dist_l_filter),(1000000,10))
pruned_ordered_list


# In[13]:


#create a metric inverted file with dictionary
metric_dict = {}
o = 0
for i in pruned_ordered_list:
  o+=1
  for j in i:
    if j in metric_dict:
      metric_dict[j].append((o, i.tolist().index(j)))
    else:
      metric_dict[j] = []
      metric_dict[j].append((o, i.tolist().index(j)))


# In[14]:


#write the metric inverted file as csv output
import csv 

with open('metric_inverted.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in metric_dict.items():
       writer.writerow([key, value])


# In[15]:


metric_dict


# In[ ]:




