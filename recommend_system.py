import userCF
import itemSet
import Apriori
import reverseTable
import train
MAX_SIMILAR_USR		=3
K_FREQUENT_ITEM		=4
FRE_ITEM_THRESH		=90
RULE_CONFID_THRESH	=0.8
TRAINSET_PORTION	=0.4
RECOMMEND_NUMBER	=10
FINAL_RESULT_PATH	='finalResult5.txt'
itemSet				=itemSet.loadItemSet()
movieInfo			=train.loadMovieInfo()
reverseTable		=reverseTable.loadReverseTable()
trainSet,testSet	=train.getTrain_TestSet(itemSet,TRAINSET_PORTION)
usrInterestItemSet	=userCF.getUserInterest(trainSet)
usrSimilarMat		=userCF.getUsrSimilarMat(usrInterestItemSet)
associationRule		=Apriori.Apriori(trainSet,K_FREQUENT_ITEM,FRE_ITEM_THRESH,RULE_CONFID_THRESH)
for usr in trainSet:
	resApriori	=train.recommend_by_Apriori(K_FREQUENT_ITEM,usr[0],associationRule,trainSet)
	resUsrCF	=train.recommend_by_uesrCF(MAX_SIMILAR_USR,usr[0],usrSimilarMat,userCF.getKNN,trainSet)
	resList		=train.mergeResult(resApriori,resUsrCF)
	resValid	=train.analysisValid(RECOMMEND_NUMBER,usr,resList,testSet,movieInfo)
	stat		=train.statistic(resValid)
	train.outPutStat(usr[0],stat,'statU3.txt')
	train.outPutRes(usr,resValid,FINAL_RESULT_PATH)
	
	resList.clear()
	resApriori.clear()
	resUsrCF.clear()