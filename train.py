def getTrain_TestSet(itemSet,TRAINSET_PORTION):
	trainSet,testSet=list(),list()
	for e in itemSet:
		count,length=1,len(e)
		limit=int(length*TRAINSET_PORTION)
		tempList=list()
		tempList.append(e[0])
		while count<=limit:
			tempList.append(e[count])
			count+=1
		trainSet.append(tempList)
		tempList=list()
		while count<length:
			tempList.append(e[count])
			count+=1
		testSet.append(tempList)
	return trainSet,testSet
def recommend_by_Apriori(K_FREQUENT_ITEM,usr,associationRule,trainSet):
	usrMovieList=list()
	for e in trainSet:
		if e[0]==usr:
			count,length=1,len(e)
			while count<length:
				usrMovieList.append(e[count][0])
				count+=1
	subSet=gen_K_realSubSet(usrMovieList,K_FREQUENT_ITEM-1)
	
			
def recommend_by_uesrCF(usr,usrSimilarMat,trainSet):
	pass
def mergeResult(resApriori,resUsrCF):
	pass
def compareWithTest(usr,resList,testSet,movieInfo):
	pass
def outPutRes(resList,resValid,movieInfo,FINAL_RESULT_PATH):
	pass
def loadMovieInfo():
	pass