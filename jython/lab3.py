##Path="C:\\Users\\yfjin\\hcss\\workresult\\Double2d\\"
##Str="Add1"
##Opt1=Double2dNumCount.Add1
##Opt2=Double2dNumCount.Add2
##Opt3=Double2dNumCount.Pow
##
##a=Double2d([[1,2,3],[2,3,4]])
##b=Double2d([[1,2,3],[2,3,4]])
##
##a+b
##a+3
###dd=Double2dNumCount.Double2dNcInput(Opt1,Str,Path)
##print dd
##Double2dNumCount.ReSet()
##Double2dNumCount.Double2dGetALL()
##Double2dNumCount.GetDimValue()
##Double2dNumCount.Double2dOptGetV(Opt1)
##Double2dNumCount.Double2dOptCount()
##Double2dNumCount.Double2dDimCount(Opt1,2,3)
##Double2dNumCount.Double2dDimGet(Opt1)
##Double2dNumCount.Double2dNcInput(Opt2,Opt2_name,Path)
#
##myGenerator1 = RandomUniform() 
##myGenerator1.setSeed(1234L)    
##a=myGenerator1(Double2d(16,16))
##import time
##timeend=0
##timebegin=time.clock()
##for i in range(16):
##	a+i
##timeend=time.clock()
##time=timeend-timebegin
##print time
##
#
#
#
## len(c) 设计一个list，在list里存储需要计算的维数
#begin=1
#step=10
#CalLength=3001
#std=range(begin,CalLength,step) # n=50
#n=(CalLength-begin)/step
#mOut=20
#mIn=100
#myGenerator = RandomUniform() 
#myGenerator.setSeed(1234L) 
#
#TimeListFor=[]
#TimeListAdd1=[]
#TimeListAdd1WithoutFor=[]
#TimeListAdd1Once=[]
#TimeListAdd1OnceJava=[]
#
#for Out in range(mOut):
#    for i in range(0,n):
#        X=myGenerator(Double1d(std[i]))
#        Y=myGenerator(Double1d(std[i]))
#        X1=X
#        Y1=Y
#
#        #for 循环变成时间花费最大的地方
#        timeAdd1Begin=time.clock()
#        for In in range(mIn):
#             X+Y
#        timeAdd1Use=time.clock()-timeAdd1Begin
#
#	#单纯for 循环的时间
#	timeForBegin=time.clock()
#	for In in range(mIn):
#	    pass
#	timeForUse=time.clock()-timeForBegin
#
#	#the Once calculate
#	timeAdd1BeginOnce=time.clock()
#	X+Y
#	timeAdd1UseOnce=time.clock()-timeAdd1BeginOnce
#
#	#Once calculate of System.nanoTime()
#
#	timeAdd1UseOnceJava=Double1dTimeCost.TimeCal("Add2",std[i])
#	
#
#	if Out==0:
#	    TimeListAdd1.append(timeAdd1Use)
#	    TimeListAdd1WithoutFor.append((timeAdd1Use-timeForUse))
#	    TimeListAdd1Once.append(timeAdd1UseOnce)
#	    TimeListAdd1OnceJava.append(timeAdd1UseOnceJava)
#	    TimeListFor.append(timeForUse)
#	   
#	else:
#	    TimeListAdd1[i]=TimeListAdd1[i]+timeAdd1Use
#	    TimeListAdd1WithoutFor[i]=TimeListAdd1WithoutFor[i]+timeAdd1Use-timeForUse
#	    TimeListAdd1Once[i]=TimeListAdd1Once[i]+timeAdd1UseOnce
#	    TimeListAdd1OnceJava[i]=TimeListAdd1OnceJava[i]+timeAdd1UseOnceJava
#	    TimeListFor[i]=TimeListFor[i]+timeForUse
#	
#for i in range(n):
#    TimeListAdd1[i]=TimeListAdd1[i]/(mOut*mIn)
#    TimeListAdd1WithoutFor[i]=TimeListAdd1WithoutFor[i]/(mOut*mIn)
#    TimeListAdd1Once[i]=TimeListAdd1Once[i]/mOut
#    TimeListAdd1OnceJava[i]=float(TimeListAdd1OnceJava[i])/(mOut)
#    TimeListFor[i]=TimeListFor[i]/(mOut*mIn)
#
#Add1TCPlot=PlotXY()
#Add1TCPlot.plotSize=(1,0)
#topLeft     = SubPlot(SubPlotGridConstraints(0,0))
#topMid      = SubPlot(SubPlotGridConstraints(1,0))
#Add1TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListAdd1),color=java.awt.Color.red)
##Add1TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListAdd1Once),color=java.awt.Color.blue)
#Add1TCLayer3 = LayerXY(Double1d(std),Double1d(TimeListAdd1WithoutFor),color=java.awt.Color.green)
#Add1TCLayer4 = LayerXY(Double1d(std),Double1d(TimeListAdd1OnceJava),color=java.awt.Color.orange)
#Add1TCLayer6 = LayerXY(Double1d(std),Double1d(TimeListAdd1OnceJava),color=java.awt.Color.orange)
#Add1TCLayer5 = LayerXY(Double1d(std),Double1d(TimeListFor),color=java.awt.Color.magenta)
#topLeft.addLayer(Add1TCLayer1)
##Add1TCPlot.addLayer(Add1TCLayer2)
#topLeft.addLayer(Add1TCLayer3)
#topLeft.addLayer(Add1TCLayer4)
#topLeft.addLayer(Add1TCLayer5)
#topMid.addLayer(Add1TCLayer6)
#Add1TCPlot.addSubPlot(topLeft)
#Add1TCPlot.addSubPlot(topMid)
#
#Add1TCLayer1.name="time cost by jython time.clock()"
##Add1TCLayer2.name="one time calculate"
#Add1TCLayer3.name="time cost by jython time.clock minus empty 'for' loop cost"
#Add1TCLayer4.name="time cost by java System.nanoTime() "
#Add1TCLayer5.name="time cost by the empty 'for' loop "
#Add1TCLayer6.name="time cost by java System.nanoTime()"
#Add1TCPlot.legend.visible = 1
#
#Add1TCPlot.titleText = "Difference time cost of the jython and java "
#Add1TCPlot.subtitleText = "by the Double1d add operator"
#topLeft.baseLayerXY.yaxis.titleText = "timecost"
#topLeft.baseLayerXY.xaxis.titleText = "data scale"
#topMid.baseLayerXY.yaxis.titleText = "timecost"
#topMid.baseLayerXY.xaxis.titleText = "data scale"
##Add1TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Add1file.png") 


A = Int2d([[1,2,3], [2,3,4]])
B = Int2d([[1,2], [2,3], [3,4]])
X = Float2d([[1,2,3], [2,3,4]])
Y = Float2d([[1,2], [2,3], [3,4]])
print A.apply(MatrixMultiplyToy(B))
print X.apply(MatrixMultiplyToy(Y))

MatrixMultiplyToy.SetGPU(True)
print A.apply(MatrixMultiplyToy(B))
print X.apply(MatrixMultiplyToy(Y))

S=Complex1d([1,2,3,4,5])
print FFT(S)

