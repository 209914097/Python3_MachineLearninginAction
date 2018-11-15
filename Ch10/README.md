### kMeans()函数算法原理：

&emsp;&emsp;一堆数据，假如要划分为A,B,C,D 4簇(即K=4)。那么先在这对数据集范围内随机生成4个簇心。然后计算所有数据到这4个簇心的距离。

&emsp;&emsp;如何把一个数据划归成A还是B还是C还是D簇呢？看这个数据离哪个簇心近，就划归给哪个簇。

&emsp;&emsp;这样，A,B,C,D 4簇都有各自的数据点了。接下来，我们要更新A,B,C,D的簇心。

> &emsp;&emsp;如何更新？以A簇为例，把A簇里面所有的数据点求和再求平均，就得到了A簇的新簇心。这就是“K均值”为什么叫“均值”，而“K”就是最终划分为“K”个簇的意思。

&emsp;&emsp;同理可得，B,C,D簇的新簇心。

&emsp;&emsp;然后，重新计算所有数据到这4个新簇心的距离，离哪个簇心距离最短的就属于那个簇。

&emsp;&emsp;这样，A,B,C,D四个簇又重新有了各自的数据点。但是，对于A簇来说，可能会出现两种情况：

&emsp;&emsp;1.	这些数据点和之前的一模一样，还是原来那些点，不多不少。

&emsp;&emsp;2.	这些数据点和之前有些不同，多了或者少了某个点。

&emsp;&emsp;同理，B,C,D簇也会出现上述两种情况。

&emsp;&emsp;若果A,B,C,D四个簇的数据点出现了情况2，即和之前有些不同，那么请像之前那样再次更新A,B,C,D的簇心。

&emsp;&emsp;一直更新到A,B,C,D四个簇的数据点都只出现情况1 ，也就是数据点稳定在各自的簇里面，铁了心永远只跟随一个簇，不会因为再次更新簇心而跑到别的簇里。

&emsp;&emsp;这时候就可以停止更新簇心了，这就是我们要找的簇心。我暂且叫它做“永恒之心My Heart Will Go On”吧！ 

### biKmeans()函数算法原理:

<img src="https://github.com/209914097/Python3_MachineLearninginAction/blob/master/Ch10/img/1.png" width="300px">

&emsp;&emsp;如上图示，首先把所有点坐标数据看做一簇，簇心为所有点坐标数据(x,y)的平均。然后计算每个点到簇心的距离，之后平方，加在一起，称之为SSE（Sum of Squared Error，误差平方和）。

&emsp;&emsp;然后，把簇一分为二，分为两簇。用什么算法分？调用kMeans()函数，令参数K=2即可。

<img src="https://github.com/209914097/Python3_MachineLearninginAction/blob/master/Ch10/img/2.png" width="600px">

&emsp;&emsp;然后遍历A簇和B簇。具体做什么呢？假如遍历到A簇，对A簇所有点调用kMeans()函数一分为二，A簇分为a,b两簇后，把a,b两个簇所有点的sse加起来得到SSE_A，SSE_A就是代码中的sseSplit变量，而B簇所有点的SSE_B就是不用一分为二的 sseNotSplit。（SSE_A+SSE_B= **`A`** ）<SSE的话，则更新SSE，否则不更新。

&emsp;&emsp;你可能会问，究竟采用把A簇一分为二，还是采用把B簇一分为二的情况。别急，上面遍历完A簇后，自然遍历B簇。

&emsp;&emsp;同样地，对B簇所有点调用kMeans()函数一分为二，B簇分为a,b两簇后，把a,b两个簇所有点的sse加起来得到SSE_B，得到代码中的sseSplit变量，而A簇所有点的SSE_A就是不用一分为二的 sseNotSplit。（SSE_B+SSE_A= **`B`** ）<SSE的话，则更新SSE，否则不更新。

&emsp;&emsp;看到这里，程序实际上把A簇一分为二，B簇一分为二两种情况都算了一遍，而最终程序会选择min（ **`A`** , **`B`** ）的一种分法，也就是若A簇一分为二的SSE比B簇一分为二情况的SSE要小，那么将采用把A簇一分为二的办法。

&emsp;&emsp;这样会得到三个簇:

<img src="https://github.com/209914097/Python3_MachineLearninginAction/blob/master/Ch10/img/3.png" width="800px">

&emsp;&emsp;然后程序会判断一下，分成3个簇是不是足够了，yes停机，No继续遍历A,B,C三个簇。怎么遍历，同上。直至到分成K个簇为止。

> bestClustAss[nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList) <br>
bestClustAss[nonzero(bestClustAss[:,0].A == 0)[0],0] = bestCentToSplit

&emsp;&emsp;这两句是用来更新索引的，比如说，原来有A,B两个簇，把B簇一分为二后，kMeans()中用0,1区分一分为二的两个簇。0,1显然不能用来指代一分为二后的两个B簇，怎么办？上面两句代码，就是把一分为二后的两个B簇更新索引为1,2.这样，索引0指代A簇，1,2指代一分为二后的两个B簇，也就是用0,1,2，指代A,B,C簇。


