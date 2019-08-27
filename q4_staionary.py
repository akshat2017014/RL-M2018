import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
import random
class arm:
    def __init__(self,arm_number,q_true,q,r,count):
        self.arm_number=arm_number
        self.q_true=q_true
        self.q=q
        self.r=r
        self.count=count
    def get_reward(self):
        return (np.random.normal(self.q_true,1))
def select_arm(epsilon,arms):
    temp=1
    while(epsilon<10 and epsilon!=0):
        epsilon*=10
        temp*=10
    temp=int(temp)
    epsilon=int(epsilon)
    num=random.randint(1,temp)
    if(num<=epsilon and epsilon!=0):
        index=random.randint(0,9)
        return (index)
    else:
        val=-111111111111
        index=-1;
        for j in range(10):
            if(arms[j].q>val):
                val=arms[j].q
                index=j
        return index
def get_optimal_action(arms):
    val=-111111111111
    index=-1;
    for j in range(10):
        if(arms[j].q_true>val):
            val=arms[j].q_true
            index=j
    return index
def select_arm_ucb(arms,total_count,c):
    val=-11111111111
    index=-1;
    for j in range(10):
        temp=arms[j].q;
        if(total_count>=1 and arms[j].count>0):
            temp+=c*math.sqrt(math.log(total_count)/arms[j].count)
        if(temp>val):
            val=temp
            index=j
    return index

arr=np.zeros([1000,2000])
optimal_action=list()
for i in range(2000):
    optimal_action.append(0)
for i in range(1000):
    arms=list()
    total_count=0;
    total_reward=0;
    for j in range(10):
        arms.append(arm(j,np.random.normal(0,1),0,0,0))
    for j in range(2000):
        for k in range(10):
            if(arms[k].count>0):
                arms[k].q=arms[k].q+(arms[k].r-arms[k].q)/arms[k].count
        arm_no=select_arm(float(0.1),arms)
        if(arm_no==get_optimal_action(arms)):
            optimal_action[j]+=1;
        arms[arm_no].r=arms[arm_no].get_reward()
        arms[arm_no].count+=1
        total_reward+=arms[arm_no].r
        total_count+=1
        arr[i,j]=total_reward/total_count
for i in range(2000):
    optimal_action[i]/=10

arr1=np.zeros([1000,2000])
optimal_action1=list()
for i in range(2000):
    optimal_action1.append(0)
for i in range(1000):
    arms=list()
    total_count=0;
    total_reward=0;
    for j in range(10):
        arms.append(arm(j,np.random.normal(0,1),5,0,0))
    for j in range(2000):
        for k in range(10):
            if(arms[k].count>0):
                arms[k].q=arms[k].q+(arms[k].r-arms[k].q)/arms[k].count
        arm_no=select_arm(0,arms)
        if(arm_no==get_optimal_action(arms)):
            optimal_action1[j]+=1;
        arms[arm_no].r=arms[arm_no].get_reward()
        arms[arm_no].count+=1
        total_reward+=arms[arm_no].r
        total_count+=1
        arr1[i,j]=total_reward/total_count
for i in range(2000):
    optimal_action1[i]/=10

arr2=np.zeros([1000,2000])
optimal_action2=list()
for i in range(2000):
    optimal_action2.append(0)
for i in range(1000):
    arms=list()
    total_count=0;
    total_reward=0;
    for j in range(10):
        arms.append(arm(j,np.random.normal(0,1),5,0,0))
    for j in range(2000):
        for k in range(10):
            if(arms[k].count>0):
                arms[k].q=arms[k].q+(arms[k].r-arms[k].q)/arms[k].count
        arm_no=select_arm_ucb(arms,total_count+1,2)
        if(arm_no==get_optimal_action(arms)):
            optimal_action2[j]+=1;
        arms[arm_no].r=arms[arm_no].get_reward()
        arms[arm_no].count+=1
        total_reward+=arms[arm_no].r
        total_count+=1
        arr2[i,j]=total_reward/total_count
for i in range(2000):
    optimal_action2[i]/=10

y=list()
y1=list()
y2=list()
for i in range(2000):
    temp=0
    temp1=0
    temp2=0
    for j in range(1000):
        temp=temp+float(arr[j][i])
        temp1=temp1+float(arr1[j][i])
        temp2=temp2+float(arr2[j][i])
    y.append(temp/1000)
    y1.append(temp1/1000)
    y2.append(temp2/1000)
x=list()
for i in range(2000):
    x.append(i+1)

plt.subplot(2,1,1)
plt.plot(x,y,'k')
plt.plot(x,y1,'y')
plt.plot(x,y2,'b')
yellow_patch = mpatches.Patch(color='yellow', label='epsilon-greedy')
black_patch = mpatches.Patch(color='black', label='Optimistic')
blue_patch = mpatches.Patch(color='blue', label='UCB')
plt.legend(handles=[yellow_patch,black_patch,blue_patch],loc=1)

plt.xlabel('steps')
plt.ylabel('average reward')

plt.subplot(2,1,2)
plt.plot(x,optimal_action,'k')
plt.plot(x,optimal_action1,'y')
plt.plot(x,optimal_action2,'b')
yellow_patch = mpatches.Patch(color='yellow', label='epsilon-greedy')
black_patch = mpatches.Patch(color='black', label='Optimistic')
blue_patch = mpatches.Patch(color='blue', label='UCB')
plt.legend(handles=[yellow_patch,black_patch,blue_patch],loc=1)

plt.xlabel('steps')
plt.ylabel('optimal_action(%)')

plt.show()