import  regression
from numpy import *
#--------------------#
# xArr,yArr=regression.loadDataSet('ex0.txt')
# ws=regression.standRegres(xArr,yArr)
# xMat=mat(xArr)
# yMat=mat(yArr)
# yHat = xMat*ws
# import matplotlib.pyplot as plt
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(xMat[:,1].flatten().A[0],yMat[0,:].flatten().A[0],s=1)
# xCopy=xMat.copy()
# xCopy.sort(0)
# yHat=xCopy*ws
# ax.plot(xCopy[:,1],yHat)
# plt.show()
#--------------------#
# xArr,yArr=regression.loadDataSet('ex0.txt')
# ws=regression.standRegres(xArr,yArr)
# xMat=mat(xArr)
# yMat=mat(yArr)
# yHat = xMat*ws
# print(corrcoef(yMat,yHat.T))
#--------------------#
# xArr, yArr = regression.loadDataSet('ex0.txt')
# yHat=regression.lwlrTest(xArr,xArr,yArr,0.003)
# xMat=mat(xArr)
# srtInd=xMat[:,1].argsort(0)
# xSort=xMat[srtInd][:,0,:]
# import matplotlib.pyplot as plt
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.plot(xSort[:,1],yHat[srtInd])
# ax.scatter(xSort[:,1].flatten().A[0],yHat[srtInd].flatten(),s=2,c='black')
# ax.scatter(xMat[:,1].flatten().A[0],mat(yArr).T.flatten().A[0],s=2,c='red')
# plt.show()
#--------------------#
# abx,aby =regression.loadDataSet('abalone.txt')
# yHat01=regression.lwlrTest(abx[0:99],abx[0:99],aby[0:99],0.1)
# yHat1=regression.lwlrTest(abx[0:99],abx[0:99],aby[0:99],1)
# yHat10=regression.lwlrTest(abx[0:99],abx[0:99],aby[0:99],10)
# print(regression.rssError(aby[0:99],yHat01.T))
# print(regression.rssError(aby[0:99],yHat1.T))
# print(regression.rssError(aby[0:99],yHat10.T))
#--------------------#
# abX,abY =regression.loadDataSet('abalone.txt')
# rightweights=regression.ridgeTest(abX,abY)
# import  matplotlib.pyplot as plt
# fig = plt.figure()
# ax=fig.add_subplot(111)
# ax.plot(rightweights)
# plt.show()
#--------------------#
# xArr,yArr =regression.loadDataSet('abalone.txt')
# regression.stageWise(xArr,yArr,0.001,5000)
# print("-------------------")
# xMat=mat(xArr)
# yMat=mat(yArr).T
# xMat=regression.regularize(xMat)
# yM = mean(yMat,0)
# yMat =yMat-yM
# weights=regression.standRegres(xMat,yMat.T)
# print(weights.T)
#--------产生图8-7的代码------------#
# xArr,yArr =regression.loadDataSet('abalone.txt')
# rightweights=regression.stageWise(xArr,yArr,0.005,1000)#运行时请把stageWise()中注释的三句代码恢复
# import  matplotlib.pyplot as plt
# fig = plt.figure()
# ax=fig.add_subplot(111)
# ax.plot(rightweights)
# plt.show()
#-------lego积木预测-------------#
import legoAPI
lgx=[];lgy=[]
legoAPI.setDataCollect(lgx,lgy)#乐高URL已经过期，所以使用legoAPI.py本地解释文件夹setHtml下的网页
# regression.scrapePage('./setHtml/lego10030.html','out.txt', 2002, 3096, 269.99)#也可以这样使用作者注释掉的scrapePage()函数
lgx1=mat(ones((63,5)))
lgx1[:,1:5]=mat(lgx)
print(lgx[0])
print(lgx1[0])
ws=regression.standRegres(lgx1,lgy)#最小二乘法，线性回归
print('ws',end='=');print(ws)
# print('lgx1[0]*ws',end='=');print(lgx1[0]*ws)
# print('lgx1[0]*ws',end='=');print(lgx1[-1]*ws)
# print('lgx1[0]*ws',end='=');print(lgx1[43]*ws)
regression.crossValidation(lgx,lgy,10)
print(regression.ridgeTest(lgx,lgy))