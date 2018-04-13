<img src="https://github.com/209914097/Python3_MachineLearninginAction/blob/master/Ch05/img/1.png" width="450px" />

&emsp;&emsp; 一条直线<a href="https://www.codecogs.com/eqnedit.php?latex=z=w_0&space;\times&space;x_0&plus;&space;w_1&space;\times&space;x_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z=w_0&space;\times&space;x_0&plus;&space;w_1&space;\times&space;x_1" title="z=w_0 \times x_0+ w_1 \times x_1" /></a>
，把上图一分为二，称之为线性回归。可以看到上面的点并不能完全通过一条直线完全区分开来。
那么，对线性方程<a href="https://www.codecogs.com/eqnedit.php?latex=z=w_0&space;\times&space;x_0&plus;&space;w_1&space;\times&space;x_1&plus;&space;\cdots&space;&plus;&space;w_n&space;\times&space;x_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z=w_0&space;\times&space;x_0&plus;&space;w_1&space;\times&space;x_1&plus;&space;\cdots&space;&plus;&space;w_n&space;\times&space;x_n" title="z=w_0 \times x_0+ w_1 \times x_1+ \cdots + w_n \times x_n" /></a>
加一个壳，也就是把z代入sigmoid函数，叫做逻辑回归。

<a href="https://www.codecogs.com/eqnedit.php?latex=g(z)=\frac{1}{(1&plus;e^{-z}&space;)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g(z)=\frac{1}{(1&plus;e^{-z}&space;)}" title="g(z)=\frac{1}{(1+e^{-z} )}"/></a>

<img src="https://github.com/209914097/Python3_MachineLearninginAction/blob/master/Ch05/img/2.jpg" width="400px" />

&emsp;&emsp; 上图是sigmoid函数图像，可以看到当z绝对值很大，g(z)输出1或者0，这刚好可以分类。

&emsp;&emsp; 在红绿粒子分类的图中，<a href="https://www.codecogs.com/eqnedit.php?latex=z=w_0&space;\times&space;x_0&plus;&space;w_1&space;\times&space;x_1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?z=w_0&space;\times&space;x_0&plus;&space;w_1&space;\times&space;x_1" title="z=w_0 \times x_0+ w_1 \times x_1" /></a>
，z绝对值越大，意味着粒子离决策直线越远，若z绝对值很大代入到g(z)，将输出1或者0，对应着正确的红绿分类。若z绝对值很小，
意味着粒子点离直线很近，这时候直线就不一定能正确分类，此时代入到g(z)，将不会输出1或者0 ，而是0.4,0.5,0.6之类的小数，
表明决策直线倾向于红还是绿的程度，若果是0.5则表明点在决策直线上，决策直线无法判断，若果是0.4则表明决策直线倾向于点为红点多一些，但不绝对是。

