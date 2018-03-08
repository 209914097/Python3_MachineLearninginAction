import trees
import matplotlib.pyplot as plt
import treePlotter
d,l= trees.createDataSet()
# print(l)
# print (d)

# print(trees.createTree(d,l))
mytree=treePlotter.retrieveTree(0)
print(trees.classify(mytree,l,[1,0]))
# print(treePlotter.getTreeDepth(mytree))
