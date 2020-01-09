#!/usr/bin/env python3

import pandas as pd
import numpy as np
from numpy import genfromtxt

MIF_Path ='C:/Users/leo.tsang/Desktop/DS8001/Untitled Folder/Q2_metric_inverted.csv'
data_path = 'C:/Users/leo.tsang/Desktop/DS8001/Untitled Folder/Q1_LEO_TSANGv2.csv'
ref_path = 'C:/Users/leo.tsang/Desktop/DS8001/Untitled Folder/ref_index.csv'

my_data = genfromtxt(data_path, delimiter=',', dtype='int')

reference = genfromtxt(ref_path, delimiter=',', dtype='int')

#reading our mif as a dataframe, later to be converted into a dictionary
mif_df = pd.read_csv(MIF_Path, header=None, sep='\n', delimiter=",")
mif_df.columns = ['a', 'b']

#convert the dataframe to a dictionary
mif_dict = dict([(i,b) for i,b in zip(mif_df.a, mif_df.b)])

#reading back the dicitonary values as the original format which are lists
for i in mif_dict.keys():
    mif_dict[i]=eval(mif_dict[i])


#taking input
a = input("Search for: ")
print('searching for [%s]' %(a))
a_new = list(eval(a))
#my test search object
#search_obj = my_data[220]
#search_obj

#creating my ordered list of reference
ordered_list_ref = []

for i in reference:
    ordered_list_ref.append(np.sum(abs(a_new-my_data[i])))
    
pruned_olr = np.argsort(ordered_list_ref)[:10]


#creating my dist query object as a dictionary
d_qo = {}

for i in pruned_olr:
    index_pos = np.where(pruned_olr==i)
    for val in mif_dict[i]:
        
        index_val = val[0] - 1 #we minus 1 to get the right index posistion to the data
        # since MIF index starts at 1 whereas python indicies starts at 0

        #calculating my accumulator value
        if index_val not in d_qo:
            d_qo[index_val] = abs(index_pos[0][0] - val[1])
        else:
            #if the object is being visisted again, it means it's a common object, therefore I'm decreasing the accumul
            #value to show that it is the most common/familiar object in our dataset
            d_qo[index_val] += abs(index_pos[0][0] - val[1]) - 0.5


#create a list of tuple so I can sort (x, y)
#x is the indicies of the object from my data, Y is my accumulator value
d_qo_list = []

for k, v1 in d_qo.items():
    d_qo_list.append((k,v1))

top_20 = sorted(d_qo_list, key=lambda x:x[1])[0:20]

for i,v in top_20:
    print(i, my_data[i])




