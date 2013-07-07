from herschel.ia.all import *
# some simple examples show you the correctness of the JCUDA
b=Int2d([[2],[3],[4]])
a=Int1d([1,2,3])
c=MatrixMultiply(b)(a)

a = Int2d([[1,2,3], [2,3,4]])
b = Int2d([[1,2], [2,3], [3,4]])
c=MatrixMultiply(a)(b)
print c
a = Float2d([[1,2,3], [2,3,4]])
b = Float2d([[1,2], [2,3], [3,4]])
c=MatrixMultiply(a)(b)
print c

import time


myGenerator1 = RandomUniform() 
myGenerator1.setSeed(1234L)                           
x = myGenerator1(Float2d(10,10))
y = myGenerator1(Float2d(10,10))
cuStartTime = time.time()
z = MatrixMultiply(x)(y)           
cuTime=time.time() - cuStartTime
xx = Double2d(x)
yy = Double2d(y)
jaStartTime = time.time()
zz = MatrixMultiply(xx)(yy)
jaTime=time.time() - jaStartTime

delta=z-zz

# compare the time of the JCUDA and pure java

timelist1=[]
timelist2=[]
# m1 means the 2^m1 elements in one dimension in the matrix 
# m2 means the times of the calculate 
m1=8
m2=10

timel1=[]
timel2=[]
for j in range(m2):
    tl1=[]
    tl2=[]
    for i in range(m1):
    	myGenerator1 = RandomUniform() 
    	#myGenerator1.setSeed(1234L)
    	n=int(Pow(i)(2));                           
    	x = myGenerator1(Double2d(n,n))
    	y = myGenerator1(Double2d(n,n))
    	cuStartTime = time.time()
    	z = MatrixMultiply1(x)(y)           
    	cuTime=time.time() - cuStartTime
    	tl1.append(cuTime)
    

    	jaStartTime = time.time()
    	zz = MatrixMultiply(x)(y)
    	jaTime=time.time() - jaStartTime
    	tl2.append(jaTime)
    timel1.append(tl1)
    timel2.append(tl2)

#calculate the average time
for i in range(0,m1):

    sum1=0.0
    sum2=0.0

    for j in range(0,m2):
	sum1=sum1+timel1[j][i]
	sum2=sum2+timel2[j][i]
    average1=sum1/m2
    average2=sum2/m2
    timelist1.append(average1)
    timelist2.append(average2)

#draw the results
import java.awt.Color

Xd=[]
for i in range(0,m1):
	n=Pow(i)(2)
	Xd.append(n)

myPlot = PlotXY()
#myPlot.width = 500
#myPlot.height = 350

myLayer1 = LayerXY(Double1d(Xd),Double1d(timelist1),color=java.awt.Color.blue)
myLayer2 = LayerXY(Double1d(Xd),Double1d(timelist2),color=java.awt.Color.red)
myLayer1.name="by JCUDA"
myLayer2.name="by pure java "
myPlot.legend.visible = 1
myPlot.addLayer(myLayer1)
myPlot.addLayer(myLayer2)


myPlot.xaxis.type = Axis.LOG
myPlot.yaxis.type = Axis.LOG

myPlot.titleText = "The Comparison with CUDA and pure Java"
myPlot.subtitleText = "The MatrixMultiply class(Double)"
myPlot.xaxis.titleText = "The number of elements in one dimension"
myPlot.yaxis.titleText = "The time used"


#myPlot.saveAsEPS("myfile.eps") # Encapsulated PS
