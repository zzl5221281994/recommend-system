from itemSet import loadItemSet
def getRealSubSet(set):
	count,length=1,2**len(set)-2
	lenSet,listSet=len(set),list(set)
	resSet=list()
	while count<=length:
		tempList=list()
		mask=bin(count).replace('0b','')
		countM,lengthM=0,len(mask)
		if lengthM<lenSet:
			mask='0'*(lenSet-lengthM)+mask
		countM,lengthM=0,len(mask)
		while countM<lengthM:
			if mask[countM]=='1':
				tempList.append(listSet[countM])
			countM+=1
		resSet.append(tempList)
		count+=1
	return resSet
def getItemSupport(itemSet,item):
	support=0
	for e in itemSet:
		count,length=1,len(e)
		tempList=list()
		while count<length:
			tempList.append(e[count][0])
			count+=1
		set1,set2=set(tempList),set(item)
		#
		#print(set1,set2)
		#
		if set1&set2==set2:
			support+=1
		tempList.clear()
	#if support>=1002:
	#	print("max")
	return support
def getOneItemSet(itemSet,threshold,supportDict):
	oneItemSet=list()
	for e in itemSet:
		count,length=1,len(e)
		while count<length:
			if e[count][0] not in supportDict:
				supportDict[e[count][0]]=1
			else:
				support=supportDict[e[count][0]]
				supportDict[e[count][0]]=support+1
			count+=1
		
	tempDic=supportDict.copy()
	keysList=tempDic.keys()
	for e in keysList:
		if tempDic[e]<threshold:
			del supportDict[e]
	tempDic.clear()
	res=list(supportDict.keys())
	res.sort()
	resList=list()
	for e in res:
		resList.append([e])
	res.clear()
	return resList
			
def genFrequentK_ItemSet(K,K_1_itemSet,threshold,supportDict,itemSet):
	pos=K-2
	resList=list()
	#print(K_1_itemSet)
	for e1 in K_1_itemSet:##link and pruning
		for e2 in K_1_itemSet:
			if e1!=e2:
				#print(e1,e2)
				E1,E2=e1.copy(),e2.copy()
				
				if E1[0:pos]==E2[0:pos] and E1[pos]<=E2[pos]:
					E1.append(E2[pos])
					resList.append(E1)
				#E1.clear()
				#E2.clear()
	#print(resList)
	#print('y',len(resList))
	testTimes=0
	resTemp=resList.copy()
	for e in resTemp:
		support=getItemSupport(itemSet,e)
		#
		#
		if support<threshold:
			testTimes+=1
			resList.remove(e)
		else:
			supportDict[tuple(e)]=support
	#
	#print('y',testTimes)
	#
	return resList

def genAssociationRule(K_itemSet,thresholdConfidence,supportDict):
	#([A],[B]):confidence,rule A->B with confidence
	resDict=dict()
	for e in K_itemSet:
		setE=set(e)
		subSet=getRealSubSet(setE)
		for sub in subSet:
			subS=set(sub)
			a,b=subS,setE-subS#A->B
			A,B,C=a.copy(),b.copy(),setE.copy()
			
			key1,key2,key3=list(A),list(B),list(C)
			key1.sort()
			key2.sort()
			key3.sort()
			#print(key1,key2,key3,'#################')
			if len(key1)==1:
				#print(type(key1[0]),'@@@@@@@@@@@@@@@@@@@@')
				resDict[key1[0]]=[key2,supportDict[tuple(key3)]/supportDict[key1[0]]]
			else:
				resDict[tuple(key1)]=[key2,supportDict[tuple(key3)]/supportDict[tuple(key1)]]
	return resDict
def Apriori(itemSet,K,thresholdItem,thresholdConfidence):
	supportDict=dict()
	K_itemSet=getOneItemSet(itemSet,thresholdItem,supportDict)#[[itemNo1,itemNo2....]...[itemNo...]]
	count,limit=2,K
	while count<=limit:
		K_itemSet=genFrequentK_ItemSet(count,K_itemSet,thresholdItem,supportDict,itemSet)#remember release K_itemSet
		count+=1
	#print(limit,K_itemSet)
	return genAssociationRule(K_itemSet,thresholdConfidence,supportDict)
	
itemSet=loadItemSet()
#itemSet=[[1,(2,3),(3,3.5),(4,4.5),(12,2.5),(13,3.5)]]
'''dic=dict()
one=getOneItemSet(itemSet,100,dic)
#print(len(itemSet))
print(len(one))
two=genFrequentK_ItemSet(2,one,100,dic,itemSet)
print(len(two))
#print(two)
three=genFrequentK_ItemSet(3,two,100,dic,itemSet)
print(len(three))
#print(three)
four=genFrequentK_ItemSet(4,three,100,dic,itemSet)
print(len(four))
#print(four)
five=genFrequentK_ItemSet(5,four,100,dic,itemSet)
print(len(five))
print(five)
#print(dic)
rule=genAssociationRule(five,0,dic)
print(rule)
itemSet=loadItemSet()
rule=Apriori(itemSet,4,100,0.5)
print(rule)'''
print(Apriori(itemSet,5,100,0))
