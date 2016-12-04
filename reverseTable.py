from itemSet import loadItemSet
def getMovieIdList(itemSet):
	movieId,dic=list(),dict()
	for e in itemSet:
		#print(e)
		count,length=1,len(e)
		while count<length:
			if e[count][0] not in dic:
				dic[e[count][0]]=''
			count+=1
	movieId=list(dic.keys())
	return movieId
def getReverseTable(itemSet):
	movieId=getMovieIdList(itemSet)
	reverseTable=dict()
	for e in movieId:
		reverseTable[e]=list()
	for e in itemSet:
		count,length=1,len(e)
		value=e[0]#value
		while count<length:
			key=e[count][0]#key movieId
			l=reverseTable[key]
			l.append(value)
			reverseTable[key]=l
			count+=1
	return reverseTable
def writeBackRevTable(reverseTable):
	fp=open('reverseTable.txt','a')
	for e in reverseTable.items():
		fp.write(str(e))
		fp.write('\n')
	fp.close()
def getKey(line):
	pos,count=1,0
	while line[count]!=',':
		count+=1
	return int(line[pos:count])
def getList(line):
	pos,count=0,0
	while line[pos]!='[':
		pos+=1
	while line[count]!=']':
		count+=1
	s=line[pos+1:count]
	l=s.split(',')
	count,length=0,len(l)
	while count<length:
		l[count]=int(l[count])
		count+=1
	return l
def loadReverseTable():
#(8,[30,113,128,182,614])
	fp=open('reverseTable.txt','r')
	reverseTable=dict()
	line=fp.readline()
	###
	times=0
	###
	while line!='' and times<4:
		times+=1
		line.replace(' ','')
		reverseTable[getKey(line)]=getList(line)
		line=fp.readline()
	return reverseTable
'''
itemSet=loadItemSet()
reverseTable=getReverseTable(itemSet)
writeBackRevTable(reverseTable)
'''