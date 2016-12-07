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
		tempList.append(e[0])
		while count<length:
			tempList.append(e[count])
			count+=1
		testSet.append(tempList)
	return trainSet,testSet
def getRecommend(usr,usr1,itemSet):
	usrList,usr1List=list(),list()
	e1,e2=None,None
	for e in itemSet:
		if e[0]==usr:
			e1=e
		if e[0]==usr1:
			e2=e
	count,length=1,len(e1)
	while count<length:
		usrList.append(e1[count][0])
		count+=1
	count,length=1,len(e2)
	while count<length:
		usr1List.append(e2[count][0])
		count+=1
	set1,set2=set(usrList),set(usr1List)
	resSet=set2-set1
	resSet=list(resSet)
	return resSet
def count1(str):
	count=0
	for e in str:
		if e=='1':
			count+=1
	return count
def gen_K_realSubSet(list1,K):
	resList=list()
	if K==0:
		return resList
	if len(list1)==0:
		return resList
	if K==1:
		for e in list1:
			resList.append([e])
		return resList
	else:
		count,length=0,len(list1)
		while count<length:
			l=gen_K_realSubSet(list1[count+1:length],K-1)
			for e in l:
				tempList=[list1[count]]
				tempList.extend(e)
				resList.append(tempList)
			count+=1
	return resList	
def recommend_by_Apriori(K_FREQUENT_ITEM,usrId,associationRule,trainSet):
	print('enter Apriori')
	usrMovieList,resList=list(),list()
	for e in trainSet:
		if e[0]==usrId:
			count,length=1,len(e)
			while count<length:
				usrMovieList.append(e[count][0])
				count+=1
			break
	print('enter genSubSet')
	usrMovieList.sort()
	subSet=gen_K_realSubSet(usrMovieList,K_FREQUENT_ITEM-1)
	print('leave genSubSet')
	for sub in subSet:
		sub.sort()
		if len(sub)==1:
			if sub[0] in associationRule:
				resList.append([[sub[0]],associationRule[sub[0]]])
		else:
			s=tuple(sub)
			if s in associationRule:
				resList.append([sub,associationRule[s]])
	usrMovieList.clear()
	print('leave Apriori')
	return resList
	#[[A],[B,confidence]] B is recommend result with confidence		
def recommend_by_uesrCF(MAX_SIMILAR_USR,usrId,usrSimilarMat,getKNN,trainSet):
	print('enter userCF')
	#userSimilarMat[(usr1Id,usr2Id)]=simi
	similarUsr=getKNN(MAX_SIMILAR_USR,usrId,usrSimilarMat)
	resList=list()
	print('similar:',similarUsr)
	for usr1 in similarUsr:
		movieList=getRecommend(usrId,usr1,trainSet)
		if (usr1,usrId) in usrSimilarMat:
			resList.append([movieList,usrSimilarMat[(usr1,usrId)]])
		else:
			resList.append([movieList,usrSimilarMat[(usrId,usr1)]])
	print('leave userCF')
	return resList
	#[[res],similarity] res is recommend result with similarity
def mergeResult(resApriori,resUsrCF):
	str1,str2='Apriori','userCF'
	resList=list()
	AprioriList,userCFlist=list(),list()
	for e in resApriori:
		AprioriList.append([e[0],e[1][0],e[1][1],str1])
	for e in resUsrCF:
		userCFlist.append([e,str2])
	AprioriList.sort(key=lambda x:x[2])
	userCFlist.sort(key=lambda x:x[1])
	for e in AprioriList:
		resList.append(e)
	for e in userCFlist:
		resList.append(e)
	return resList
def analysisValid(RECOMMEND_NUMBER,usr,resList,testSet,movieInfo):
	pass
	
def outPutRes(usr,resValid,FINAL_RESULT_PATH):
	pass
def loadMovieInfo():
	fp=open('movies.txt','r')
	resDict=dict()
	line=fp.readline()
	line=fp.readline()
	while line!='':
		l=line.split('\t')
		resDict[int(l[0])]=[l[1],l[2]]
		line=fp.readline()
	return resDict
#set1=[1,2,3,4,5,6,7,8,9,0,10,11,12,13,15,16,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
#list1=[1,2,3,4]
#print(gen_K_realSubSet(set1,2))