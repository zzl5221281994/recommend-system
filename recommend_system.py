import userCF
import itemSet
import Apriori
import reverseTable
import train
MAX_SIMILAR_USR		=2
K_FREQUENT_ITEM		=4
FRE_ITEM_THRESH		=110
RULE_CONFID_THRESH	=0.5
TRAINSET_PORTION	=0.6
RECOMMEND_NUMBER	=10
FINAL_RESULT_PATH	='finalResult.txt'
itemSet				=itemSet.loadItemSet()
#
#print(itemSet)
#
movieInfo			=train.loadMovieInfo()
#
#print(movieInfo)
#
reverseTable		=reverseTable.loadReverseTable()
#
#
trainSet,testSet	=train.getTrain_TestSet(itemSet,TRAINSET_PORTION)
#
#print(trainSet)
#print('########################')
#print(testSet)
#
usrInterestItemSet	=userCF.getUserInterest(trainSet)
#
#print(usrInterestItemSet)
#
usrSimilarMat		=userCF.getUsrSimilarMat(usrInterestItemSet)
#
#print(usrSimilarMat)
#
associationRule		=Apriori.Apriori(trainSet,K_FREQUENT_ITEM,FRE_ITEM_THRESH,RULE_CONFID_THRESH)
#
print(associationRule)
#

for usr in trainSet:
	print('usr:',usr[0])
	resApriori	=train.recommend_by_Apriori(K_FREQUENT_ITEM,usr[0],associationRule,trainSet)
	#print('###################rule:',usr[0],associationRule)
	print('###################Apriori:',usr[0],resApriori)
	resUsrCF	=train.recommend_by_uesrCF(MAX_SIMILAR_USR,usr[0],usrSimilarMat,userCF.getKNN,trainSet)
	###
	#print(resApriori)
	#print('##########################')
	print('###################usrCF:',usr[0],resUsrCF)
	###
	resList		=train.mergeResult(resApriori,resUsrCF)
	print('###################resList:',usr[0],resList)
	resValid	=train.analysisValid(RECOMMEND_NUMBER,usr,resList,testSet,movieInfo)
	train.outPutRes(usr,resValid,FINAL_RESULT_PATH)
	
	resApriori.clear()
	resUsrCF.clear()