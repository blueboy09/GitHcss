import time
# len(c) 设计一个list，在list里存储需要计算的维数
begin=1
step=10
CalLength=3001
std=range(begin,CalLength,step) # n=50
n=(CalLength-begin)/step
mOut=100
mIn=100
myGenerator = RandomUniform() 
myGenerator.setSeed(1234L) 

TimeListAdd1=[]
TimeListAdd1WithoutFor=[]
TimeListAdd1Once=[]
TimeListAdd1OnceJava=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(Double1d(std[i]))
        X1=X
        Y1=Y

        #for 循环变成时间花费最大的地方
        timeAdd1Begin=time.clock()
        for In in range(mIn):
             X+Y
        timeAdd1Use=time.clock()-timeAdd1Begin

	#单纯for 循环的时间
	timeForBegin=time.clock()
	for In in range(mIn):
	    pass
	timeForUse=time.clock()-timeForBegin

	#the Once calculate
	timeAdd1BeginOnce=time.clock()
	X+Y
	timeAdd1UseOnce=time.clock()-timeAdd1BeginOnce

	#Once calculate of System.nanoTime()
	timeAdd1BeginOnceJava=System.nanoTime()
	X+Y
	timeAdd1UseOnceJava=System.nanoTime()-timeAdd1BeginOnceJava
	

	if Out==0:
	    TimeListAdd1.append(timeAdd1Use)
	    TimeListAdd1WithoutFor.append((timeAdd1Use-timeForUse))
	    TimeListAdd1Once.append(timeAdd1UseOnce)
	    TimeListAdd1OnceJava.append(timeAdd1UseOnceJava)
	   
	else:
	    TimeListAdd1[i]=TimeListAdd1[i]+timeAdd1Use
	    TimeListAdd1WithoutFor[i]=TimeListAdd1WithoutFor[i]+timeAdd1Use-timeForUse
	    TimeListAdd1Once[i]=TimeListAdd1Once[i]+timeAdd1UseOnce
	    TimeListAdd1OnceJava[i]=TimeListAdd1OnceJava[i]+timeAdd1UseOnceJava
	
for i in range(n):
    TimeListAdd1[i]=TimeListAdd1[i]/(mOut*mIn)
    TimeListAdd1WithoutFor[i]=TimeListAdd1WithoutFor[i]/(mOut*mIn)
    TimeListAdd1Once[i]=TimeListAdd1Once[i]/mOut
    TimeListAdd1OnceJava[i]=float(TimeListAdd1OnceJava[i])/(mOut*1000000000)

Add1TCPlot=PlotXY()
Add1TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListAdd1),color=java.awt.Color.blue)
Add1TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListAdd1Once),color=java.awt.Color.red)
Add1TCLayer3 = LayerXY(Double1d(std),Double1d(TimeListAdd1WithoutFor),color=java.awt.Color.green)
Add1TCLayer4 = LayerXY(Double1d(std),Double1d(TimeListAdd1OnceJava),color=java.awt.Color.orange)
Add1TCPlot.addLayer(Add1TCLayer1)
Add1TCPlot.addLayer(Add1TCLayer2)
Add1TCPlot.addLayer(Add1TCLayer3)
Add1TCPlot.addLayer(Add1TCLayer4)

Add1TCLayer1.name="with time of internal for circulation"
Add1TCLayer2.name="one time calculate"
Add1TCLayer3.name="deduct the time of internal 'for circulation' "
Add1TCLayer4.name="one time calculate count by System.nanoTime' "
Add1TCPlot.legend.visible = 1

Add1TCPlot.titleText = "the Time Used of the Double1d Add1 Operation"
Add1TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
Add1TCPlot.yaxis.titleText = "timeused"
#Add1TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Add1file.png") 
#　定义一个函数