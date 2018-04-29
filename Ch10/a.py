from numpy import *
import matplotlib.pyplot as plt

x=arange(0,10,0.1)  # [ 0.   0.1  0.2 ...,  9.7  9.8  9.9]

y=random.randn(len(x))

fig = plt.figure()
ax = fig.add_subplot(2,1,1)
ax.plot(x,y)
ax = fig.add_subplot(2,2,1,frameon=False)
ax.plot(x,y)
plt.show()
