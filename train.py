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
	if len(usrMovieList)>200:
		return []
	subSet=list()
	count,length=1,K_FREQUENT_ITEM-1
	while count<=length:
		subSet.extend(gen_K_realSubSet(usrMovieList,count))
		count+=1
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
	subSet.clear()
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
	similarUsr.clear()
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
	AprioriList.sort(key=lambda x:x[2],reverse=True)
	userCFlist.sort(key=lambda x:x[1],reverse=True)
	for e in AprioriList:
		resList.append(e)
	for e in userCFlist:
		resList.append(e)
	return resList
def listToStr(lis):
	s=''
	count=0
	for e in lis:
		if count<=1:
			s+=str(e).ljust(10)
		elif count==2:
			s+=str(e).ljust(60)
		elif count==3:
			s+=str(e).rjust(60).replace('\n','')+'\t'
		else:
			s+=str(e)+'\t\t'
		count+=1
	return s
def getRecommendList(resList):
	res=list()
	#print(resList)
	#print('@@###@@@@@#####@@')
	for e in resList:
		if len(e)==4:
			rule=[e[0],e[1],e[2]]
			#print(rule)
			for id in e[1]:
				res.append([id,'Apriori',rule])
		if len(e)==2:
			for id in e[0][0]:
				res.append([id,'user_CF',e[0][1]])
	return res
def addMovieInfo(recList,movieInfo):
	for e in recList:
		id=e[0]
		res=movieInfo[id]
		name,catagory=res[0],res[1]
		e.insert(1,catagory)
		e.insert(1,name)
	return recList
def checkTest(recList,tempList):
	for e in recList:
		id=e[0]
		mark=0
		for mId in tempList:
			if mId==id:
				mark=1
				break
		if mark==1:
			e.insert(0,'YES')
		else:
			e.insert(0,'NO')
	return recList
		
def analysisValid(RECOMMEND_NUMBER,usr,resList,testSet,movieInfo):
	recList=getRecommendList(resList)
	#id,Apriori,rule:confidence
	#id,user_CF,similarity
	recList=addMovieInfo(recList,movieInfo)
	#print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',recList)
	#id,name,catagory,Apriori,rule,confidence
	#id,name,catagory,user_CF,similarity
	tempList=list()
	for e in testSet:
		if e[0]==usr[0]:
			count,length=1,len(e)
			while count<length:
				tempList.append(e[count][0])
				count+=1
			break
	recList=checkTest(recList,tempList)
	#YES,id,name,catagory,Apriori,rule,confidence
	#NO ,id,name,catagory,user_CF,similarity
	return recList
def statistic(recList):
	count1,count2=0,0
	for e in recList:
		if e[0]=='YES':
			if e[4]=='Apriori':
				count1+=1
			else:
				count2+=1
	return [['Apriori',count1],['user_CF',count2]]
def outPutStat(usrNo,recList,filename):
	s=str(usrNo)+' '+str(recList[0][1])+' '+str(recList[1][1])+'\n'
	fp=open(filename,'a')
	fp.write(s)
	fp.close()
def outPutRes(usr,resValid,FINAL_RESULT_PATH):
	fp=open(FINAL_RESULT_PATH,'a')
	title='$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$usrId:'+str(usr)
	print('begin write')
	#print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$',resValid)
	fp.write(title+'\n')
	for e in resValid:
		s=listToStr(e)
		fp.write(s+'\n')
	fp.write('\n\n')
	fp.close()
	print('end write')
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
'''subSet=list()
count,length=1,4-1
while count<=length:
	subSet.extend(gen_K_realSubSet([1,2,3,4],count))
	count+=1
print(subSet)'''