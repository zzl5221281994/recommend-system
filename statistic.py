FILE1='statU'
FILE2='.txt'
FILE_NUM=1
resList=list()
while FILE_NUM<=3:
	fp=open(FILE1+str(FILE_NUM)+FILE2,'r')
	line=fp.readline()
	countApriori,countUserCF=0,0
	AprioriUser,userCFUser,AllUser=0,0,0
	while line!='':
		l=line.split(' ')
		count,length=0,len(l)
		while count<length:
			l[count]=int(l[count])
			count+=1
		if l[1]>0 and l[2]==0:#Apriori only
			countApriori+=l[1]
			AprioriUser+=1
		if l[1]==0 and l[2]>0:#userCF only
			countUserCF+=l[2]
			userCFUser+=1
		if l[1]>0 and l[2]>0:#all
			countApriori+=l[1]
			countUserCF+=l[2]
			AllUser+=1
		line=fp.readline()
	resList.append([FILE_NUM,countApriori,countUserCF,AprioriUser,userCFUser,AllUser])
	fp.close()
	FILE_NUM+=1
tempList1,tempList2,tempList3=list(),list(),list()
for e in resList:
	tempList1.append(e[1])
	tempList2.append(e[2])
	tempList3.append(e[1]+e[2])
tupleApriori,tupleUserCF,tupleAll=tuple(tempList1),tuple(tempList2),tuple(tempList3)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
fig1 = plt.figure(2)
rects1 =plt.bar(left = (0.2,1.0,1.8),height = tupleApriori,color=('g'),label=(('Apriori')),width = 0.2,align="center",yerr=0.000001)
rects2 =plt.bar(left = (0.4,1.2,2.0),height = tupleUserCF,color=('r'),label=(('userCF')),width = 0.2,align="center",yerr=0.000001)
rects3 =plt.bar(left = (0.6,1.4,2.2),height = tupleAll,color=('b'),label=(('Sum')),width = 0.2,align="center",yerr=0.000001)
plt.legend()
plt.xticks((0.4,1.2,2.0),('userNumber=2','userNumber=3','userNumber=4'))
plt.title('Hit movie Number')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()

