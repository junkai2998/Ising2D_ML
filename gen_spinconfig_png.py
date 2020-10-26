### generate png of spin configuration at all temperature

import os
import numpy as np
import matplotlib.pyplot as plt
from IPython import display

cwd=os.getcwd()
temp=os.listdir(cwd+'\data')
print('*** temp=',temp)
print('set j between 0 to '+str(len(temp)-1))
#j=10
#j=len(temp)-1 #specify j in 0 till len(temp)-1 to visualise the configurations for temperature=temp[j

#### abstract L #####
tempti='data/'+temp[0]
cdir=cwd+'/'+tempti
for dum in range(10):
    if os.listdir(cdir)[dum][-3:] == 'dat':
        i=os.listdir(cdir)[dum]
        f = open(cdir+'/'+i, "r+")
        st=f.readline()
        #print(st)
        s1=str.split(st,'; N_run')[0]
        L=int(str.split(s1,"=")[1])
        #print("L=",L)
print("L=",L)
#### end of abstract L #####

for j in range(len(temp)):
    #tempti='data/'+temp[j]    
    tempti='data/0.001'
    cdir=cwd+'/'+tempti
    rawdata=np.empty(shape=[len(os.listdir(cdir)),L,L])
    for i in os.listdir(cdir):
        if i[-3:] != 'png':
#        rawdata[count]=np.loadtxt(cdir+'/'+i,skiprows=0)
            rawdata=np.loadtxt(cdir+'/'+i,skiprows=0)
        #count=count+1
            name=i[:-4]
            plt.imshow(rawdata,cmap=plt.cm.hot)
            plt.savefig(cdir+'/'+name+'.png')
            print(cdir+'/'+name+'.png'+' created')