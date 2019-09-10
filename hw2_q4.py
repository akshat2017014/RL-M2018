#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random


# Necessary header files

# In[42]:


def policy_evaluation(v_s,pi_s,theeta,gamma):
    counter=0
    while(True):
        delta=0;
        for i in range(5):
            for j in range(5):
                v=v_s[i,j]
                new_v_s=0
                if(i==0  and j==1):
                    new_v_s+=1*(10+gamma*v_s[4,1])
                elif(i==0 and j==3):
                    new_v_s+=1*(5+gamma*v_s[2,3])
                else:
                    if(pi_s[i,j]==0):
                        if(i-1>=0):
                            new_v_s+=1*(gamma*v_s[i-1,j])
                        else:
                            new_v_s+=1*(-1+gamma*v_s[i,j])
                    elif(pi_s[i,j]==1):
                        if(j+1<=4):
                            new_v_s+=1*(gamma*v_s[i,j+1])
                        else:
                            new_v_s+=1*(-1+gamma*v_s[i,j])
                    elif(pi_s[i,j]==2):
                        if(i+1<=4):
                            new_v_s+=1*(gamma*v_s[i+1,j])
                        else:
                            new_v_s+=1*(-1+gamma*v_s[i,j])
                    elif(pi_s[i,j]==3):
                        if(j-1>=0):
                            new_v_s+=1*(gamma*v_s[i,j-1])
                        else:
                            new_v_s+=1*(-1+gamma*v_s[i,j])
                v_s[i,j]=new_v_s
                delta=max(delta,abs(v-new_v_s))
        if(delta<theeta):
            break


    
        


# In[43]:


def policy_improvement(v_s,pi_s,gamma):
    policy_stable=True
    for i in range(5):
        for j in range(5):
            old_action=pi_s[i,j]
            new_policy=pi_s[i,j]
            max=-9999999
            if(((i!=0 or j!=1) and  (i!=0 or j!=3))):
                temp=0
                if(i-1>=0):
                    temp=1*(gamma*v_s[i-1,j])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=0
                if(j+1<=4):
                    temp=1*(gamma*v_s[i,j+1])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=1       
                if(i+1<=4):
                    temp=1*(gamma*v_s[i+1,j])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=2
                if(j-1>=0):
                    temp=1*(gamma*v_s[i,j-1])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=3
            pi_s[i,j]=new_policy
            if(old_action!=new_policy):
                policy_stable=False
    return policy_stable


# In[44]:


v_s=np.zeros([5,5])
pi_s=np.zeros([5,5]);
theeta=0.000000001
gamma=0.9
policy_evaluation(v_s,pi_s,theeta,gamma)
while(policy_improvement(v_s,pi_s,gamma)==False):
    policy_evaluation(v_s,pi_s,theeta,gamma)

print("Value function:")
print(v_s)
print("Policy Selected:")
print(pi_s)


#  v_s[i,j] and pi_s[i,j] represents expected reward and policy repectively, corresponding to each state.

# policies:
# 0->up
# 1->right
# 2->down
# 3->left

# In[ ]:




