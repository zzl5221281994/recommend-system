def getDataSet(filePath):
	res=list()
	fp=open(filePath,'r')
	line=fp.readline()
	line=fp.readline()
	while line!='':
		temp=line.split(',')
		count,length=0,len(temp)
		while count<length:
			if count!=2:
				temp[count]=int(temp[count])
			else:
				temp[count]=float(temp[count])
			count+=1
		res.append(temp)
		line=fp.readline()
	return res
		
def getItemSet(dataSet):
	dataSet.sort(key=lambda x:x[0])
	count,length=1,len(dataSet)
	itemSet=list()
	p=-1
	while count<length:
		if dataSet[count][0]==p:
			tempList.append((dataSet[count][1],dataSet[count][2]))
		else:
			if p!=-1:
				itemSet.append(tempList)
			tempList=list()
			p=dataSet[count][0]
			tempList.append(dataSet[count][0])
			tempList.append((dataSet[count][1],dataSet[count][2]))
		count+=1
	itemSet.append(tempList)
	return itemSet
data=getDataSet('ratings.csv')
item=getItemSet(data)

fp=open('itemSet.txt','w')
for e in item:
	count,length=0,len(e)
	while count<length:
		e[count]=str(e[count])
		count+=1
	fp.write(','.join(e))
	fp.write('\n')
	
			
		

		
	
		