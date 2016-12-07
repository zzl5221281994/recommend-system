import userCF
import itemSet
import Apriori
import reverseTable
import train
MAX_SIMILAR_USR		5
K_FREQUENT_ITEM		5
FRE_ITEM_THRESH		150
RULE_CONFID_THRESH	0.9
TRAINSET_PORTION	0.5
FINAL_RESULT_PATH	'finalResult.txt'
itemSet				=loadItemSet()
movieInfo			=loadMovieInfo()
reverseTable		=loadReverseTable()
trainSet,testSet	=getTrain_TestSet(itemSet)
usrInterestItemSet	=getUserInterest(trainSet)
usrSimilarMat		=getUsrSimilarMat(usrInterestItemSet)
associationRule		=Apriori(usrInterestItemSet,K_FREQUENT_ITEM,FRE_ITEM_THRESH,RULE_CONFID_THRESH)
for usr in trainSet:
	resApriori	=recommend_by_Apriori(usr,associationRule,trainSet)
	resUsrCF	=recommend_by_uesrCF(usr,usrSimilarMat,trainSet)
	resList		=mergeResult(resApriori,resUsrCF)
	recomValid	=compareWithTest(usr,resList,testSet,movieInfo)
	resValid	=analysisValid(recomValid)
	outPutRes(resList,resValid,movieInfo,FINAL_RESULT_PATH)