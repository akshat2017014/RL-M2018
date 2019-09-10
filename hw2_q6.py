#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random


# Necessary header files

# In[6]:


def policy_evaluation(v_s,pi_s,theeta,gamma):
    counter=0
    while(True):
        delta=0;
        for i in range(4):
            for j in range(4):
                v=v_s[i,j]
                new_v_s=0
                if(i==0  and j==0):
                    new_v_s+=0
                elif(i==3 and j==3):
                    new_v_s+=0
                else:
                    if(pi_s[i,j]==0):
                        if(i-1>=0):
                            new_v_s+=1*(-1+gamma*v_s[i-1,j])
                        else:
                            new_v_s+=1*(-1+gamma*v_s[i,j])
                    elif(pi_s[i,j]==1):
                        if(j+1<=3):
                            new_v_s+=1*(-1+gamma*v_s[i,j+1])
                        else:
                            new_v_s+=1*(-1+gamma*v_s[i,j])
                    elif(pi_s[i,j]==2):
                        if(i+1<=3):
                            new_v_s+=1*(-1+gamma*v_s[i+1,j])
                        else:
                            new_v_s+=1*(-1+gamma*v_s[i,j])
                    elif(pi_s[i,j]==3):
                        if(j-1>=0):
                            new_v_s+=1*(-1+gamma*v_s[i,j-1])
                        else:
                            new_v_s+=1*(-1+gamma*v_s[i,j])
                v_s[i,j]=new_v_s
                delta=max(delta,abs(v-new_v_s))
        if(delta<theeta):
            break


    
        


# In[7]:


def policy_improvement(v_s,pi_s,gamma):
    policy_stable=True
    for i in range(4):
        for j in range(4):
            old_action=pi_s[i,j]
            new_policy=pi_s[i,j]
            max=-9999999
            if(((i!=0 or j!=0) and  (i!=3 or j!=3))):
                temp=0
                if(i-1>=0):
                    temp=1*(-1+gamma*v_s[i-1,j])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=0
                if(j+1<=3):
                    temp=1*(-1+gamma*v_s[i,j+1])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=1       
                if(i+1<=3):
                    temp=1*(-1+gamma*v_s[i+1,j])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=2
                if(j-1>=0):
                    temp=1*(-1+gamma*v_s[i,j-1])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=3
            pi_s[i,j]=new_policy
            if(old_action!=new_policy):
                policy_stable=False
    return policy_stable


# In[8]:


def policy_iteration():
    print("----policy_iteartion----")
    v_s=np.zeros([4,4])
    pi_s=np.zeros([4,4]);
    theeta=0.000000001
    gamma=0.9
    policy_evaluation(v_s,pi_s,theeta,gamma)
    counter=1;
    while(policy_improvement(v_s,pi_s,gamma)==False):
        print("iteration No.",counter,":")
        print("Value function:")
        print(v_s)
        print("Policy Selected:")
        print(pi_s)
        print()
        counter+=1
        policy_evaluation(v_s,pi_s,theeta,gamma)
    print("iteration No.",counter,":")
    print("Value function:")
    print(v_s)
    print("Policy Selected:")
    print(pi_s)
    print()


#  v_s[i,j] and pi_s[i,j] represents expected reward and policy repectively, corresponding to each state.

# policies:
# 0->up
# 1->right
# 2->down
# 3->left

# The order in which we are checking for optimal policy in policy improvement is same, thus in case of two policies having same expected value convergence is always possible.

# In[9]:


def deterministic_policy(v_s,pi_s,gamma):
    for i in range(4):
        for j in range(4):
            max=-9999999
            if(((i!=0 or j!=0) and  (i!=3 or j!=3))):
                temp=0
                if(i-1>=0):
                    temp=1*(-1+gamma*v_s[i-1,j])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=0
                if(j+1<=3):
                    temp=1*(-1+gamma*v_s[i,j+1])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=1       
                if(i+1<=3):
                    temp=1*(-1+gamma*v_s[i+1,j])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=2
                if(j-1>=0):
                    temp=1*(-1+gamma*v_s[i,j-1])
                else:
                    temp=1*(-1+gamma*v_s[i,j])
                if(temp>max):
                    max=temp
                    new_policy=3
                pi_s[i,j]=new_policy


# In[26]:


def value_iteration():
    v_s=np.zeros([4,4])
    pi_s=np.zeros([4,4]);
    theeta=0.00000001
    gamma=0.9
    while(True):
        delta=0;
        for i in range(4):
            for j in range(4):
                v=v_s[i,j]
                new_v=v_s[i,j]
                max1=-9999999
                if(((i!=0 or j!=0) and  (i!=3 or j!=3))):
                    temp=0
                    if(i-1>=0):
                        temp=1*(-1+gamma*v_s[i-1,j])
                    else:
                        temp=1*(-1+gamma*v_s[i,j])
                    if(temp>max1):
                        max1=temp
                        new_policy=0
                    if(j+1<=3):
                        temp=1*(-1+gamma*v_s[i,j+1])
                    else:
                        temp=1*(-1+gamma*v_s[i,j])
                    if(temp>max1):
                        max1=temp
                        new_policy=1       
                    if(i+1<=3):
                        temp=1*(-1+gamma*v_s[i+1,j])
                    else:
                        temp=1*(-1+gamma*v_s[i,j])
                    if(temp>max1):
                        max1=temp
                        new_policy=2
                    if(j-1>=0):
                        temp=1*(-1+gamma*v_s[i,j-1])
                    else:
                        temp=1*(-1+gamma*v_s[i,j])
                    if(temp>max1):
                        max1=temp
                        new_policy=3
                    new_v=max1
                v_s[i,j]=new_v
                delta=max(delta,abs(v-new_v))
        if(delta<theeta):
            break
    deterministic_policy(v_s,pi_s,gamma)
    print("----value_iteartion----")
    print("Value function:")
    print(v_s)
    print("Policy Selected:")
    print(pi_s)
    print()
                    


# In[27]:


policy_iteration()
value_iteration()


# In[ ]:




