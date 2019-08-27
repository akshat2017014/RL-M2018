import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

optimal_action=list()
for i in range(1000):
    optimal_action.append(0)
for i in range(1000):
    arms=list()
    for j in range(10):
        arms.append(arm(j,np.random.normal(0,1),5,0,0))
    for j in range(1000):
        for k in range(10):
            arms[k].q_true+=np.random.normal(0,0.01)
            if(arms[k].count>0):
                arms[k].q=arms[k].q+(arms[k].r-arms[k].q)*0.1
        arm_no=select_arm(0,arms)
        if(arm_no==get_optimal_action(arms)):
            optimal_action[j]+=1;
        arms[arm_no].r=arms[arm_no].get_reward()
        arms[arm_no].count+=1
for i in range(1000):
    optimal_action[i]/=10


optimal_action1=list()
for i in range(1000):
    optimal_action1.append(0)
for i in range(1000):
    arms=list()
    for j in range(10):
        arms.append(arm(j,np.random.normal(0,1),0,0,0))
    for j in range(1000):
        for k in range(10):
            arms[k].q_true+=np.random.normal(0,0.01)
            if(arms[k].count>0):
                arms[k].q=arms[k].q+(arms[k].r-arms[k].q)*0.1
        arm_no=select_arm(float(0.1),arms)
        if(arm_no==get_optimal_action(arms)):
            optimal_action1[j]+=1;
        arms[arm_no].r=arms[arm_no].get_reward()
        arms[arm_no].count+=1
for i in range(1000):
    optimal_action1[i]/=10

x=list()
for i in range(1000):
    x.append(i+1)

plt.plot(x,optimal_action,'k')
plt.plot(x,optimal_action1,'y')
yellow_patch = mpatches.Patch(color='yellow', label='Realistic')
black_patch = mpatches.Patch(color='black', label='optimistic')
plt.legend(handles=[yellow_patch,black_patch],loc=1)
plt.xlabel('steps')
plt.ylabel('optimal_action(%)')

plt.show()

