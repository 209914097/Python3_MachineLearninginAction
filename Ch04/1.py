import  bayes
p,c = bayes.loadDataSet()
#
# v = bayes.createVocabList(p)
# h=bayes.setOfWords2Vec(v,['dog','do'])
# # print(h)
# # trainMat=[]
# # for Doc in p:
# #     trainMat.append(bayes.setOfWords2Vec(v,Doc))
# # p0v,p1v,pAb=bayes.trainNB0(trainMat,c)
# # print(pAb)
# bayes.testingNB()
# mysent = 'This book is the best book on Python or  M.L. I have ever laid eyes upon.'
# mysent.split()
# import re
# regex = re.compile('\\W+')
# ltoken = regex.split(mysent)
# tok = [token.lower() for token in ltoken if len(token)>0]
# print(tok)
bayes.spamTest()
