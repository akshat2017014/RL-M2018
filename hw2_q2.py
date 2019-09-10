#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random


# from a given state we can only go to four states with a fixed reward for each state, thus in rhs of bellman equation we will get only four terms.Let s1,s2,s3,s4 be the states we can go from s, then equation would be:
# v(s)=1/4( (sum of reward of going from s to s1,s2,s3 and s4) + (gamma)*(v(s1)+v(s2)+v(s3)+v(s4))

# In[2]:


equations=np.zeros([25,25])
coff=np.zeros([25])
gamma=0.9
for i in range(5):
    for j in range(5):
        if(i==0 and j==1):
            coff[5*i+j]=10
            equations[5*i+j,1]=1
            equations[5*i+j,21]=(-1)*(gamma)
        elif(i==0 and j==3):
            coff[5*i+j]=5
            equations[5*i+j,3]=1
            equations[5*i+j,13]=-1*(gamma)
        else:
            sum_reward=0;
            equations[5*i+j,5*i+j]=4
            if(i-1>=0):
                equations[5*i+j,(i-1)*5+j]=(-1)*(gamma)
            else:
                sum_reward-=1;
                equations[5*i+j,(i)*5+j]+=(-1)*(gamma)
            if(i+1<=4):
                equations[5*i+j,(i+1)*5+j]=(-1)*(gamma)
            else:
                sum_reward-=1;
                equations[5*i+j,(i)*5+j]+=(-1)*(gamma)
            if(j-1>=0):
                equations[5*i+j,(i)*5+(j-1)]=(-1)*(gamma)
            else:
                sum_reward-=1;
                equations[5*i+j,(i)*5+j]+=(-1)*(gamma)
            if(j+1<=4):
                equations[5*i+j,(i)*5+(j+1)]=(-1)*(gamma)
            else:
                sum_reward-=1;
                equations[5*i+j,(i)*5+j]+=(-1)*(gamma)
            coff[5*i+j]=sum_reward
            
# print(coff)
# print(equations)
ans = np.linalg.solve(equations, coff)
ans = np.resize(ans, (5,5))
print(ans)
    
        


# states are row major (state i,j=5*i+j)
# gamma=0.9
