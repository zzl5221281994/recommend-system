import re
def writeBack(itemSet):
	fp=open('itemSet.txt','a')
	for e in itemSet:
		count,length=0,len(e)
		while count<length:
			e[count]=str(e[count])
			count+=1
		fp.write(','.join(e))
		fp.write('\n')
	fp.flush()
	fp.close()
def getItemSet(dataSet):
	dataSet.sort(key=lambda x:x[0])
	count,length=0,len(dataSet)
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
	
def getDataSet(filePath):
	times=0
	res,countPos=list(),0
	fp=open(filePath,'r')
	line=fp.readline()
	line=fp.readline()
	p=int(line[0])
	while line!='':
		temp=line.split(',')
		count,length=0,len(temp)
		while count<length:
			if count!=2:
				temp[count]=int(temp[count])
			else:
				temp[count]=float(temp[count])
			count+=1
		
		if temp[0]!=p:
			itemSet=getItemSet(res)
			writeBack(itemSet)
			itemSet.clear()
			res.clear()
			p=temp[0]
			times+=1
		res.append(temp)
		line=fp.readline()
	itemSet=getItemSet(res)
	writeBack(itemSet)
	itemSet.clear()
	res.clear()
	times+=1
	return times
def genTuple(str):
	count,length=0,len(str)
	while str[count]!=',':
		count+=1
	item1=int(str[1:count])
	pos=count+1
	while str[count]!=')':
		count+=1
	item2=float(str[pos:count])
	return (item1,item2)
def parseLine(str):
	pos,count,length=0,0,len(str)
	l=list()
	while str[count]!=',':
		count+=1
	l.append(int(str[pos:count]))
	count+=1
	while count<length:
		if str[count]!='(':
			return -1
		pos=count
		while str[count]!=')':
			count+=1
		count+=1
		l.append(genTuple(str[pos:count]))
		count+=1
	return l

def loadItemSet():
	itemSet=list()
	fp=open('itemSet.txt','r')
	line=fp.readline()
	regex='\d+,(\(\d+,\d+\.\d+\))(,(\(\d+,\d+\.\d+\)))*'
	pattern=re.compile(regex)
	##
	times=0
	##
	while line!='':
		times+=1
		##
		line=line.replace(' ','')
		match=pattern.match(line[0:-1])
		if match!=None:
			l=parseLine(line[0:-1])
			if l!=-1:
				itemSet.append(l)
		line=fp.readline()
	return itemSet
#getDataSet('ratings.csv')	