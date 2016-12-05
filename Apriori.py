def getRealSubSet(set):
	pass
def getItemSupport(itemSet,item):
	support=0
	for e in itemSet:
		count,length=1,len(e)
		tempList=list()
		while count<length:
			tempList.append(e[count][0])
			count+=1
		set1,set2=set(tempList),set(item)
		if set1&set2==set2:
			support+=1
		tempList.clear()
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
		
	tempDic,keysList=supportDict.copy(),supportDict.keys()
	for e in keysList:
		if tempDic[e]<threshold:
			del supportDict[e]
	tempDic.clear()
	return supportDict.keys().sort()
			
def genFrequentK_ItemSet(K,K_1_itemSet,threshold,supportDict,itemSet):
	pos=K-2
	resList=list()
	for e1 in K_1_itemSet:##link and pruning
		for e2 in K_1_itemSet:
			if e1!=e2:
				if e1[0:pos]==e2[0:pos] and e1[pos]<=e2[pos]:
					resList.append(e1.extend(e2[pos]))
	for e in resList:
		support=getItemSupport(itemSet,e)
		if support<threshold:
			resList.remove(e)
		else:
			supportDict[e]=support
	return resList

def genAssociationRule(K_itemSet,supportDict):
	resDict=dict()
	for e in K_itemSet:
		set1=set(e)
		realSubSet=getRealSubSet(set1)
		for set2 in realSubSet:
			A,B=set2,set1-set2
			resDict[[list(A),list(B)]]=supportDict[list(set1)]/supportDict[list(A)]#association rule
		realSubSet.clear()
	return resDict
def Apriori(itemSet,K):
	supportDict=dict()
	K_itemSet=getFrequentOneItemSet(itemSet,threshold,supportDict)#[itemNo1,itemNo2....]
	count,limit=2,K
	while count<=limit:
		K_itemSet=genFrequentK_ItemSet(count,K_itemSet,threshold,supportDict)#remember release K_itemSet
		count+=1
	#[[A],[B]]:confidence,rule A->B with confidence
	return genAssociationRule(K_itemSet,supportDict)
	
	pass
def 