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

# add1
TimeListAdd1=[]
TimeListAdd1Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(1)


        #for循环累计
        timeAdd1Begin=time.clock()
        for In in range(mIn):
             X+Y
        timeAdd1Use=time.clock()-timeAdd1Begin


	#the Once calculate
	timeAdd1BeginOnce=time.clock()
	X+Y
	timeAdd1UseOnce=time.clock()-timeAdd1BeginOnce
	

	if Out==0:
	    TimeListAdd1.append(timeAdd1Use)
	    TimeListAdd1Once.append(timeAdd1UseOnce)
	   
	else:
	    TimeListAdd1[i]=TimeListAdd1[i]+timeAdd1Use
	    TimeListAdd1Once[i]=TimeListAdd1Once[i]+timeAdd1UseOnce
	
for i in range(n):
    TimeListAdd1[i]=TimeListAdd1[i]/(mOut*mIn)
    TimeListAdd1Once[i]=TimeListAdd1Once[i]/mOut

Add1TCPlot=PlotXY()
Add1TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListAdd1),color=java.awt.Color.blue)
Add1TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListAdd1Once),color=java.awt.Color.red)

Add1TCPlot.addLayer(Add1TCLayer1)
Add1TCPlot.addLayer(Add1TCLayer2)

Add1TCLayer1.name="with time of internal for circulation"
Add1TCLayer2.name="one time calculate"
Add1TCPlot.legend.visible = 1

Add1TCPlot.titleText = "the Time Used of the Double1d Add1 Operation"
Add1TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
Add1TCPlot.yaxis.titleText = "The timeused"
Add1TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Add1Time.png") 

# add2
TimeListAdd2=[]
TimeListAdd2Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(Double1d(std[i]))


        #for循环累计
        timeAdd2Begin=time.clock()
        for In in range(mIn):
             X+Y
        timeAdd2Use=time.clock()-timeAdd2Begin


	#the Once calculate
	timeAdd2BeginOnce=time.clock()
	X+Y
	timeAdd2UseOnce=time.clock()-timeAdd2BeginOnce
	

	if Out==0:
	    TimeListAdd2.append(timeAdd2Use)
	    TimeListAdd2Once.append(timeAdd2UseOnce)
	   
	else:
	    TimeListAdd2[i]=TimeListAdd2[i]+timeAdd2Use
	    TimeListAdd2Once[i]=TimeListAdd2Once[i]+timeAdd2UseOnce
	
for i in range(n):
    TimeListAdd2[i]=TimeListAdd2[i]/(mOut*mIn)
    TimeListAdd2Once[i]=TimeListAdd2Once[i]/mOut

Add2TCPlot=PlotXY()
Add2TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListAdd2),color=java.awt.Color.blue)
Add2TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListAdd2Once),color=java.awt.Color.red)

Add2TCPlot.addLayer(Add2TCLayer1)
Add2TCPlot.addLayer(Add2TCLayer2)

Add2TCLayer1.name="with time of internal for circulation"
Add2TCLayer2.name="one time calculate"
Add2TCPlot.legend.visible = 1

Add2TCPlot.titleText = "the Time Used of the Double1d Add2 Operation"
Add2TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
Add2TCPlot.yaxis.titleText = "The timeused"
Add2TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Add2Time.png") 

#sub1
TimeListSub1=[]
TimeListSub1Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(1)

        #for循环累计
        timeSub1Begin=time.clock()
        for In in range(mIn):
             X-Y
        timeSub1Use=time.clock()-timeSub1Begin


	#the Once calculate
	timeSub1BeginOnce=time.clock()
	X-Y
	timeSub1UseOnce=time.clock()-timeSub1BeginOnce
	

	if Out==0:
	    TimeListSub1.append(timeSub1Use)
	    TimeListSub1Once.append(timeSub1UseOnce)
	   
	else:
	    TimeListSub1[i]=TimeListSub1[i]+timeSub1Use
	    TimeListSub1Once[i]=TimeListSub1Once[i]+timeSub1UseOnce
	
for i in range(n):
    TimeListSub1[i]=TimeListSub1[i]/(mOut*mIn)
    TimeListSub1Once[i]=TimeListSub1Once[i]/mOut

Sub1TCPlot=PlotXY()
Sub1TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListSub1),color=java.awt.Color.blue)
Sub1TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListSub1Once),color=java.awt.Color.red)

Sub1TCPlot.addLayer(Sub1TCLayer1)
Sub1TCPlot.addLayer(Sub1TCLayer2)

Sub1TCLayer1.name="with time of internal for circulation"
Sub1TCLayer2.name="one time calculate"
Sub1TCPlot.legend.visible = 1

Sub1TCPlot.titleText = "the Time Used of the Double1d Sub1 Operation"
Sub1TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
Sub1TCPlot.yaxis.titleText = "The timeused"
Sub1TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Sub1Time.png") 

#sub2
TimeListSub2=[]
TimeListSub2Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(Double1d(std[i]))
        #for循环累计
        timeSub2Begin=time.clock()
        for In in range(mIn):
             X-Y
        timeSub2Use=time.clock()-timeSub2Begin


	#the Once calculate
	timeSub2BeginOnce=time.clock()
	X-Y
	timeSub2UseOnce=time.clock()-timeSub2BeginOnce
	

	if Out==0:
	    TimeListSub2.append(timeSub2Use)
	    TimeListSub2Once.append(timeSub2UseOnce)
	   
	else:
	    TimeListSub2[i]=TimeListSub2[i]+timeSub2Use
	    TimeListSub2Once[i]=TimeListSub2Once[i]+timeSub2UseOnce
	
for i in range(n):
    TimeListSub2[i]=TimeListSub2[i]/(mOut*mIn)
    TimeListSub2Once[i]=TimeListSub2Once[i]/mOut

Sub2TCPlot=PlotXY()
Sub2TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListSub2),color=java.awt.Color.blue)
Sub2TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListSub2Once),color=java.awt.Color.red)

Sub2TCPlot.addLayer(Sub2TCLayer1)
Sub2TCPlot.addLayer(Sub2TCLayer2)

Sub2TCLayer1.name="with time of internal for circulation"
Sub2TCLayer2.name="one time calculate"
Sub2TCPlot.legend.visible = 1

Sub2TCPlot.titleText = "the Time Used of the Double1d Sub2 Operation"
Sub2TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
Sub2TCPlot.yaxis.titleText = "The timeused"
Sub2TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Sub2Time.png") 

#mul1
TimeListMul1=[]
TimeListMul1Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(1)

        #for循环累计
        timeMul1Begin=time.clock()
        for In in range(mIn):
             X*Y
        timeMul1Use=time.clock()-timeMul1Begin


	#the Once calculate
	timeMul1BeginOnce=time.clock()
	X*Y
	timeMul1UseOnce=time.clock()-timeMul1BeginOnce
	

	if Out==0:
	    TimeListMul1.append(timeMul1Use)
	    TimeListMul1Once.append(timeMul1UseOnce)
	   
	else:
	    TimeListMul1[i]=TimeListMul1[i]+timeMul1Use
	    TimeListMul1Once[i]=TimeListMul1Once[i]+timeMul1UseOnce
	
for i in range(n):
    TimeListMul1[i]=TimeListMul1[i]/(mOut*mIn)
    TimeListMul1Once[i]=TimeListMul1Once[i]/mOut

Mul1TCPlot=PlotXY()
Mul1TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListMul1),color=java.awt.Color.blue)
Mul1TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListMul1Once),color=java.awt.Color.red)

Mul1TCPlot.addLayer(Mul1TCLayer1)
Mul1TCPlot.addLayer(Mul1TCLayer2)

Mul1TCLayer1.name="with time of internal for circulation"
Mul1TCLayer2.name="one time calculate"
Mul1TCPlot.legend.visible = 1

Mul1TCPlot.titleText = "the Time Used of the Double1d Mul1 Operation"
Mul1TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
Mul1TCPlot.yaxis.titleText = "The timeused"
Mul1TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Mul1Time.png") 

#mul2
TimeListMul2=[]
TimeListMul2Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(Double1d(std[i]))

        #for循环累计
        timeMul2Begin=time.clock()
        for In in range(mIn):
             X*Y
        timeMul2Use=time.clock()-timeMul2Begin


	#the Once calculate
	timeMul2BeginOnce=time.clock()
	X*Y
	timeMul2UseOnce=time.clock()-timeMul2BeginOnce
	

	if Out==0:
	    TimeListMul2.append(timeMul2Use)
	    TimeListMul2Once.append(timeMul2UseOnce)
	   
	else:
	    TimeListMul2[i]=TimeListMul2[i]+timeMul2Use
	    TimeListMul2Once[i]=TimeListMul2Once[i]+timeMul2UseOnce
	
for i in range(n):
    TimeListMul2[i]=TimeListMul2[i]/(mOut*mIn)
    TimeListMul2Once[i]=TimeListMul2Once[i]/mOut

Mul2TCPlot=PlotXY()
Mul2TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListMul2),color=java.awt.Color.blue)
Mul2TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListMul2Once),color=java.awt.Color.red)

Mul2TCPlot.addLayer(Mul2TCLayer1)
Mul2TCPlot.addLayer(Mul2TCLayer2)

Mul2TCLayer1.name="with time of internal for circulation"
Mul2TCLayer2.name="one time calculate"
Mul2TCPlot.legend.visible = 1

Mul2TCPlot.titleText = "the Time Used of the Double1d Mul2 Operation"
Mul2TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
Mul2TCPlot.yaxis.titleText = "The timeused"
Mul2TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Mul2Time.png") 

#div1
TimeListDiv1=[]
TimeListDiv1Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(1)

        #for循环累计
        timeDiv1Begin=time.clock()
        for In in range(mIn):
             X/Y
        timeDiv1Use=time.clock()-timeDiv1Begin


	#the Once calculate
	timeDiv1BeginOnce=time.clock()
	X/Y
	timeDiv1UseOnce=time.clock()-timeDiv1BeginOnce
	

	if Out==0:
	    TimeListDiv1.append(timeDiv1Use)
	    TimeListDiv1Once.append(timeDiv1UseOnce)
	   
	else:
	    TimeListDiv1[i]=TimeListDiv1[i]+timeDiv1Use
	    TimeListDiv1Once[i]=TimeListDiv1Once[i]+timeDiv1UseOnce
	
for i in range(n):
    TimeListDiv1[i]=TimeListDiv1[i]/(mOut*mIn)
    TimeListDiv1Once[i]=TimeListDiv1Once[i]/mOut

Div1TCPlot=PlotXY()
Div1TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListDiv1),color=java.awt.Color.blue)
Div1TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListDiv1Once),color=java.awt.Color.red)

Div1TCPlot.addLayer(Div1TCLayer1)
Div1TCPlot.addLayer(Div1TCLayer2)

Div1TCLayer1.name="with time of internal for circulation"
Div1TCLayer2.name="one time calculate"
Div1TCPlot.legend.visible = 1

Div1TCPlot.titleText = "the Time Used of the Double1d Div1 Operation"
Div1TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
Div1TCPlot.yaxis.titleText = "The timeused"
Div1TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Div1Time.png") 


#div2
TimeListDiv2=[]
TimeListDiv2Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(Double1d(std[i]))

        #for循环累计
        timeDiv2Begin=time.clock()
        for In in range(mIn):
             X/Y
        timeDiv2Use=time.clock()-timeDiv2Begin


	#the Once calculate
	timeDiv2BeginOnce=time.clock()
	X/Y
	timeDiv2UseOnce=time.clock()-timeDiv2BeginOnce
	

	if Out==0:
	    TimeListDiv2.append(timeDiv2Use)
	    TimeListDiv2Once.append(timeDiv2UseOnce)
	   
	else:
	    TimeListDiv2[i]=TimeListDiv2[i]+timeDiv2Use
	    TimeListDiv2Once[i]=TimeListDiv2Once[i]+timeDiv2UseOnce
	
for i in range(n):
    TimeListDiv2[i]=TimeListDiv2[i]/(mOut*mIn)
    TimeListDiv2Once[i]=TimeListDiv2Once[i]/mOut

Div2TCPlot=PlotXY()
Div2TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListDiv2),color=java.awt.Color.blue)
Div2TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListDiv2Once),color=java.awt.Color.red)

Div2TCPlot.addLayer(Div2TCLayer1)
Div2TCPlot.addLayer(Div2TCLayer2)

Div2TCLayer1.name="with time of internal for circulation"
Div2TCLayer2.name="one time calculate"
Div2TCPlot.legend.visible = 1

Div2TCPlot.titleText = "the Time Used of the Double1d Div2 Operation"
Div2TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
Div2TCPlot.yaxis.titleText = "The timeused"
Div2TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\Div2Time.png") 

#abs

#neg

#pow

#mod

#dotproduct1
TimeListDotProduct1=[]
TimeListDotProduct1Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(Double1d(std[i]))



	#the Once calculate
	timeDotProduct1BeginOnce=time.clock()
	X.dotProduct(Y)
	timeDotProduct1UseOnce=time.clock()-timeDotProduct1BeginOnce
	

	if Out==0:
	    #TimeListDotProduct1.append(timeDotProduct1Use)
	    TimeListDotProduct1Once.append(timeDotProduct1UseOnce)
	   
	else:
	    #TimeListDotProduct1[i]=TimeListDotProduct1[i]+timeDotProduct1Use
	    TimeListDotProduct1Once[i]=TimeListDotProduct1Once[i]+timeDotProduct1UseOnce
	
for i in range(n):
    #TimeListDotProduct1[i]=TimeListDotProduct1[i]/(mOut*mIn)
    TimeListDotProduct1Once[i]=TimeListDotProduct1Once[i]/mOut

DotProduct1TCPlot=PlotXY()
#DotProduct1TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListDotProduct1),color=java.awt.Color.blue)
DotProduct1TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListDotProduct1Once),color=java.awt.Color.red)

#DotProduct1TCPlot.addLayer(DotProduct1TCLayer1)
DotProduct1TCPlot.addLayer(DotProduct1TCLayer2)

#DotProduct1TCLayer1.name="with time of internal for circulation"
DotProduct1TCLayer2.name="one time calculate"
DotProduct1TCPlot.legend.visible = 1

DotProduct1TCPlot.titleText = "the Time Used of the Double1d DotProduct1 Operation"
DotProduct1TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
DotProduct1TCPlot.yaxis.titleText = "The timeused"
DotProduct1TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\DotProduct1Time.png") 

#dotproduct2
TimeListDotProduct2=[]
TimeListDotProduct2Once=[]

for Out in range(mOut):
    for i in range(0,n):
        X=myGenerator(Double1d(std[i]))
        Y=myGenerator(Double2d(std[i],std[i]))


	#the Once calculate
	timeDotProduct2BeginOnce=time.clock()
	X.dotProduct(Y)
	timeDotProduct2UseOnce=time.clock()-timeDotProduct2BeginOnce
	

	if Out==0:
	    #TimeListDotProduct2.append(timeDotProduct2Use)
	    TimeListDotProduct2Once.append(timeDotProduct2UseOnce)
	   
	else:
	    #TimeListDotProduct2[i]=TimeListDotProduct2[i]+timeDotProduct2Use
	    TimeListDotProduct2Once[i]=TimeListDotProduct2Once[i]+timeDotProduct2UseOnce
	
for i in range(n):
    #TimeListDotProduct2[i]=TimeListDotProduct2[i]/(mOut*mIn)
    TimeListDotProduct2Once[i]=TimeListDotProduct2Once[i]/mOut

DotProduct2TCPlot=PlotXY()
#DotProduct2TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListDotProduct2),color=java.awt.Color.blue)
DotProduct2TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListDotProduct2Once),color=java.awt.Color.red)

#DotProduct2TCPlot.addLayer(DotProduct2TCLayer1)
DotProduct2TCPlot.addLayer(DotProduct2TCLayer2)

#DotProduct2TCLayer1.name="with time of internal for circulation"
DotProduct2TCLayer2.name="one time calculate"
DotProduct2TCPlot.legend.visible = 1

DotProduct2TCPlot.titleText = "the Time Used of the Double1d DotProduct2 Operation"
DotProduct2TCPlot.xaxis.titleText = "The Array Scale of the Double1d"
DotProduct2TCPlot.yaxis.titleText = "The timeused"
DotProduct2TCPlot.saveAsPNG("C:\Users\yfjin\hcss\workresult\DotProduct2Time.png") 

#outproduct




#　定义一个函数