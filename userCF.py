from itemSet import loadItemSet
from reverseTable import getReverseTable
import reverseTable
def cosSimilarity(usrItemList1,usrItemList2):
	set1,set2=set(usrItemList1),set(usrItemList2)
	return len(set1&set2)/math.sqrt(len(set1)*len(set2))
	
def getList(item):
	count,length=1,len(item)
	resList=list()
	while count<length:
		resList.append(item[count][0])
		count+=1
	return resList
def getUserInterest(itemSet):
	resItemSet=list()
	for e in itemSet:
		count,length=1,len(e)
		averageScore,tempList=0,list()
		tempList.append(e[0])
		while count<length:
			averageScore+=e[count][1]
			count+=1
		averageScore=averageScore/(length-1)
		count=1
		while count<length:
			if e[count][1]>=averageScore:
				tempList.append(e[count])
			count+=1
		resItemSet.append(tempList)
	return resItemSet
def getUsrSimilarMat():
	itemSet=loadItemSet()
	userInterestItemSet=getUserInterest(itemSet)#
	revSearchTable=getReverseTable(userInterestItemSet)#
	#(userId1,userId2):relation
	userSimilarMat=dict()
	markmat		  =dict()
	for usr1 in userInterestItemSet:
		for usr2 in userInterestItemSet:
			usr1Id,usr2Id=usr1[0],usr2[0]
			if (usr1Id,usr2Id) not in markmat and (usr2Id,usr1Id) not in markmat:
				markmat[(usr1Id,usr2Id)]=1
				simi=cosSimilarity(getList(usr1),getList(usr2))
				if simi>0:
					userSimilarMat[(usr1Id,usr2Id)]=simi
	markmat.clear()
	return userSimilarMat		
	
def getKNN(K,usrId,userSimilarMat):
	pairedId=userSimilarMat.keys()
	simiList,resList=list()
	for e in pairedId:
		if e[0]==usrId or e[1]==usr1Id:
			simiList.append([e,userSimilarMat[e]])
	simiList.sort(key=lambda x:x[1])
	count=0
	while count<K:
		if simiList[count][0][0]==usrId:
			resList.append(simiList[count][0][1])
		else:
			resList.append(simiList[count][0][0])
	simiList.clear()
	return resList 
	