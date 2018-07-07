import regTrees
from numpy import *
# testMat=mat(eye(4))
# mat0,mat1=regTrees.binSplitDataSet(testMat,1,0.5)
# print(mat0)
# print(mat1)
#https://blog.csdn.net/sinat_17196995/article/details/69621687
# myDat=regTrees.loadDataSet('ex0.txt')
# MyMat=mat(myDat)
# print(regTrees.createTree(MyMat))

#----------------------- 图9-1 基于CART算法构建回归树的简单数据集
# import matplotlib.pyplot as plt
# myDat=regTrees.loadDataSet('ex00.txt')
# myMat=mat(myDat)
# plt.xlim(-0.2,1.2)
# plt.ylim(-1,2)
# plt.plot(myMat[:,0],myMat[:,1],'ro')
# plt.show()

#-----------------------图9-2 用于测试回归树的分段常数数据集
# import matplotlib.pyplot as plt
# myDat1=regTrees.loadDataSet('ex0.txt')
# myMat1=mat(myDat1)
# plt.xlim(-0.2,1.2)
# plt.ylim(-1,5)
# plt.plot(myMat1[:,1],myMat1[:,2],'ro')
# plt.show()

# ----------------------预剪枝--------
# myDat=regTrees.loadDataSet('ex2.txt')
# MyMat=mat(myDat)
# print(regTrees.createTree(MyMat,ops=(10000,4)))

# ----------------------后剪枝--------
# myDat2=regTrees.loadDataSet('ex2.txt')
# MyMat2=mat(myDat2)
# myTree=regTrees.createTree(MyMat2,ops=(0,1))
# myDatTest=regTrees.loadDataSet('ex2test.txt')
# myMat2Test=mat(myDatTest)
# print(regTrees.prune(myTree,myMat2Test))

# ----------------------模型树---------
# myMat2=mat(regTrees.loadDataSet('exp2.txt'))
# print(regTrees.createTree(myMat2,regTrees.modelLeaf,regTrees.modelErr,(1,10)))

#--------------------- 图9-4 用来测试模型树构建函数的分段线性数据
# import matplotlib.pyplot as plt
# myDat1=regTrees.loadDataSet('exp2.txt')
# myMat1=mat(myDat1)
# plt.xlim(-0.2,1.2)
# plt.ylim(2,14)
# plt.scatter(myMat1[:,0].A,myMat1[:,1].A,c='r',marker='o',s=5)
# plt.show()

#--------------------- 图9-6 人们骑自行车的速度和他们智商之间的关系数据。
# import matplotlib.pyplot as plt
# myDat1=regTrees.loadDataSet('bikeSpeedVsIq_train.txt')
# myMat1=mat(myDat1)
# plt.xlim(-5,25)
# plt.ylim(0,200)
# plt.scatter(myMat1[:,0].A,myMat1[:,1].A,c='r',marker='o',s=5)
# plt.show()
# --------------------- 红点是训练数据，蓝点是测试数据
# import matplotlib.pyplot as plt
# myDat1=regTrees.loadDataSet('bikeSpeedVsIq_train.txt')
# myMat1=mat(myDat1)
# myDat2=regTrees.loadDataSet('bikeSpeedVsIq_test.txt')
# myMat2=mat(myDat2)
# plt.xlim(-5,25)
# plt.ylim(0,200)
# plt.scatter(myMat1[:,0].A,myMat1[:,1].A,c='r',marker='o',s=5)
# plt.scatter(myMat2[:,0].A,myMat2[:,1].A,c='b',marker='x',s=6)
# plt.show()
# # --------------------- 树回归与标准回归的比较
# trainMat = mat(regTrees.loadDataSet('bikeSpeedVsIq_train.txt'))
# testMat = mat(regTrees.loadDataSet('bikeSpeedVsIq_test.txt'))
# myTree = regTrees.createTree(trainMat,ops = (1,20))
# yHat = regTrees.createForeCast(myTree,testMat[:,0])
# print(len(set(yHat[:,0].T.tolist()[0])))#yHat实际上就是训练集按树回归分堆之后，各堆对应的平均值，测试集按这个回归树分堆，分到哪堆，它的预测值就是哪堆的平均值
#                                         #因为测试集很可能有很多数据被回归树分到同一堆，因此这时它的预测值就会出现相同的情况，这句代码采用set可以去除重复数据，yHat有200个数据，去除重复后只有7个
# print(corrcoef(yHat,testMat[:,1],rowvar=0)[0,1])
# --------------------- 红点是训练数据，蓝点是测试数据，黄点是回归树预测数据，黄点预测数据有很多是重复的，因此一个黄点可能是多个黄点重合得到
# import matplotlib.pyplot as plt
# myDat1=regTrees.loadDataSet('bikeSpeedVsIq_train.txt')
# myMat1=mat(myDat1)
# myDat2=regTrees.loadDataSet('bikeSpeedVsIq_test.txt')
# myMat2=mat(myDat2)
# plt.xlim(-5,25)
# plt.ylim(0,200)
# plt.scatter(myMat1[:,0].A,myMat1[:,1].A,c='r',marker='o',s=5)
# plt.scatter(myMat2[:,0].A,myMat2[:,1].A,c='b',marker='x',s=6)
# plt.scatter(myMat2[:,0].A,yHat[:,0].A,c='y',marker='s',s=6)
# plt.show()

# myTree2 = regTrees.createTree(trainMat,regTrees.modelLeaf,regTrees.modelErr,(1,20))
# yHat2 = regTrees.createForeCast(myTree2,testMat[:,0],regTrees.modelTreeEval)
# print(corrcoef(yHat2,testMat[:,1],rowvar=0)[0,1])
#
# ws,X,Y, = regTrees.linearSolve(trainMat)
# yHat3=mat(ones((200,1)))
# for i in range(shape(testMat)[0]):
#     yHat3[i]=testMat[i,0]*ws[1,0]+ws[0,0]
# print(corrcoef(yHat3,testMat[:,1],rowvar=0)[0,1])
# --------绿线是标准回归拟合 红点是训练数据，蓝点是测试数据，黑点是模型树预测数据，模型树有7个叶端，因此可以隐约看到7条直线拟合-------------
# import matplotlib.pyplot as plt
# myDat1=regTrees.loadDataSet('bikeSpeedVsIq_train.txt')
# myMat1=mat(myDat1)
# myDat2=regTrees.loadDataSet('bikeSpeedVsIq_test.txt')
# myMat2=mat(myDat2)
# plt.xlim(-5,25)
# plt.ylim(0,200)
# plt.scatter(myMat1[:,0].A,myMat1[:,1].A,c='r',marker='o',s=5)
# plt.scatter(myMat2[:,0].A,myMat2[:,1].A,c='b',marker='x',s=6)
# plt.scatter(myMat2[:,0].A,yHat2[:,0].A,c='black',marker='s',s=6)
# plt.plot(myMat2[:,0].A,yHat3[:,0].A,c='g')
# plt.show()

from  tkinter import  *

# ------Tkinter的Hello World----------
# root = Tk()
# myLabel = Label(root,text='hello world!')
# myLabel.grid()
# root.mainloop()
# ------程序清单9-6----------
def reDraw(tolS,tolN):
    pass
def drawNewTree():
    pass
root = Tk()
Label(root,text='图表放置').grid(row=0,columnspan=3)
Label(root,text='tolN').grid(row=1,column=0)
tolNentry = Entry(root)
tolNentry.grid(row=1,column=1)
tolNentry.insert(8,'10')
Label(root,text='tolS').grid(row=2,column=0)
tolSentry = Entry(root)
tolSentry.grid(row=2,column=1)
tolSentry.insert(0,'1.0')
Button(root,text='ReDraw',command=drawNewTree).grid(row=1,column=2,rowspan=3)
chkBtnVar = IntVar()
chkBtn = Checkbutton(root,text='Model Tree',variable=chkBtnVar)
chkBtn.grid(row=3,column=0,columnspan=2)
reDraw.rawDat = mat(regTrees.loadDataSet('sine.txt'))
reDraw.testDat = arange(min(reDraw.rawDat[:,0]),max(reDraw.rawDat[:,0]),0.01)
reDraw(1.0,10)
Button(root,text='Quit',fg="black",command=root.quit).grid(row=1,column=2)
root.mainloop()