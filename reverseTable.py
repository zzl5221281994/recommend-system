from itemSet import loadItemSet
def getMovieIdList():
	fp=open('movies.csv','r')
	movieId=list()
	line=fp.readline()
	while line!='':
		l=line.split(',')
		movieId.append(int(l[0]))
		line=fp.readline()
	return movieId
def getReverseTable(itemSet):
	movieId=getMovieIdList()
	reverseTable=dict()
	for e in movieId:
		reverseTable[e]=''
	for e in itemSet:
		count,length=1,len(e)
		value=e[0]#id
		while count<length:
			key=e[count][0]#id
			tempStr=reverseTable[key]
			tempStr=tempStr+str(value)+' '
			reverseTable[key]=tempStr
			count+=1
'''
itemSet=list()
fp=open('itemSet.txt','r')
line=fp.readline()
count=0
while count<5:
	print(line)
	line=fp.readline()
	count+=1
'''
		