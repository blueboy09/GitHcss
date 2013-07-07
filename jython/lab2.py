# lab 2 
# try the import method
#import os
#print os.getcwd()
#from herschel.ia.all import *
#import sys
#sys.path.append("C:\\Users\\yfjin\\hcss\\workspace\\")
#import MatrixTry

#a=Double1d([1,2,3])
#b=Double1d([1,2,3,4])
#c=Double1d([1,3])
#d=Double1d([1,2,3,4,3,4,2,3,4,5,6,7])
#e=Double1d([1,2,3,4,3,4])
#d.add(3)
#e.add(3)
#a.add(2)
#b.add(2)
#c.add(2)
#aa1=Double1dNumCount.Double1dGetDtl(Double1dNumCount.Add1)
#aa=Double1dNumCount.Double1dGetDim(aa1)
#print Long1d(aa)
#ss=Double1dNumCount.Double1dGetDtl(Double1dNumCount.Add1)
#print Long2d(ss)
#Double1dNumCount.Double1dGetALL()
#
#num=8192*2;
#myGenerator1 = RandomUniform() 
#myGenerator1.setSeed(1234L)                           
#re = myGenerator1(Double1d(num))
#im = myGenerator1(Double1d(num))
#X=Complex1d(re,im)
#CudaFFT(X)
#import time
#timebegin=time.clock()
#for i in range(70000):
#    CudaFFT(X)
#timeend=time.clock()-timebegin
#print timeend
#Ops="NCfft"
#import time
#t1=time.clock()
#s=FFTTimeCost.TimeCal(Ops,40000)
#t2=time.clock()
#t=t2-t1
#print t
#FFTNumCount.FFTGetALL()
#ss=FFTNumCount.FFTGetDtl(FFTNumCount.NCfft)
#s=Long2d(ss)
#print s
#dd=FFTNumCount.FFTGetDtl(FFTNumCount.NCifft)
#d=Long2d(dd)
#print d
#t1=time.clock()
#s=FFTTimeCost.TimeCal(Ops,131072)
#t2=time.clock()
#t=t2-t1
#print t

#
#SmallPipelineTimeUsed={"Add1":0,"Add2":0,"Sub1":0,"Sub2":0,"Mul1":0,"Mul2":0,"Div1":0,"Div2":0,"Pow":0,"Neg":0,"Abs":0,"Mod":0,"DotProduct1":0,"DotProduct2":0,"OutProduct":0}
#Operation=["Add1","Add2","Sub1","Sub2","Mul1","Mul2","Div1","Div2","Pow","Neg","Abs","Mod","DotProduct1"]
#OptArray=[Double1dNumCount.Add1,Double1dNumCount.Add2,Double1dNumCount.Sub1,Double1dNumCount.Sub2,\
#	   Double1dNumCount.Mul1,Double1dNumCount.Mul2,Double1dNumCount.Div1,Double1dNumCount.Div2,\
#	   Double1dNumCount.Pow,Double1dNumCount.Neg,Double1dNumCount.Mod,Double1dNumCount.Abs,\
#	   Double1dNumCount.DotProduct1,Double1dNumCount.DotProduct2,Double1dNumCount.OutProduct]
#Path="C:\\Users\\yfjin\\hcss\\workresult\\Double1d\\"
#SPTimeUsed=[]
#AllTime=0
#for Opt in Operation:
#    OptTimeUsed=Double1dTimeCost.TimeCost(Opt,Path)
#    AllTime=AllTime+OptTimeUsed
#    SPTimeUsed.append(OptTimeUsed)
#    SmallPipelineTimeUsed[Opt]=OptTimeUsed
#
#print AllTime
#print SmallPipelineTimeUsed
#fp = open(Path+"result.txt",'w')
#print >> fp, SmallPipelineTimeUsed
#print >> fp, "AllTime = ", AllTime
#fp.close()
#
#myPlot = PlotXY()
#myLayer1 = LayerXY(Double1d(range(len(Operation))),Double1d(SPTimeUsed),color=java.awt.Color.blue)
#myLayer1.name="real time used of Spectrometer pipeline" 
#myPlot.addLayer(myLayer1)
#myPlot.legend.visible =0
#myPlot.titleText = "real time used of Spectrometer map pipeline" 
#myPlot.xaxis.titleText = "Variety of the Calculate Operation"
#myPlot.yaxis.titleText = "Time Used"
#myPlot.saveAsPNG(Path+"AllOptTime.png")
#myPlot.close()



from herschel.ia.numeric.toolbox.basic import Histogram
from herschel.ia.numeric.toolbox.basic import BinCentres
d = Double1d(200000,10)
d[99000:110000] = 15
d[99900:101000] = 20.0
rnd = RandomGauss()
for ix in range(200000):
   d[ix] += rnd.calc(1.0)
p1 = PlotXY (d)
binsize = STDDEV (d) * 2.35
print binsize
hist = Histogram(binsize)
bins = BinCentres(binsize)
p2 = PlotXY(bins(d),hist(d))
# or you could try:  p = PlotXY (Histogram(binsize), BinCentres (binSize))
p2.style.chartType = Style.HISTOGRAM


x=Double1d([1,2,3,4,5,6,7,8,9])
y=x*x
x1=x
x2=x
x3=x
y1=y-1
y2=y+1
y3=y+3
myPlot = PlotXY()
#myPlot.batch = 1
myLayer1 = LayerXY(x,y)
myLayer2 = LayerXY(x1,y1)
myLayer3 = LayerXY(x2,y2)
myLayer4 = LayerXY(x3,y3) 
myPlot.addLayer(myLayer1, 1, 1)
#myPlot.addLayer(myLayer2, 0, 1)
myPlot.addLayer(myLayer3, 1, 0)
myPlot.addLayer(myLayer4, 1, 1)
myPlot.batch = 0

#　定义一个函数
p.plotSize=(2,2)
# Set the positions for the subplots in a grid layout
topLeft     = SubPlot(SubPlotGridConstraints(0,0))
bottomLeft  = SubPlot(SubPlotGridConstraints(0,1))
topMid      = SubPlot(SubPlotGridConstraints(1,0))
bottomMid   = SubPlot(SubPlotGridConstraints(1,1))
topRight    = SubPlot(SubPlotGridConstraints(2,0))
bottomRight = SubPlot(SubPlotGridConstraints(2,1))


# Display legends
p.legend.visible=1	
p.legend.columns=1
p.legend.position=PlotLegend.CUSTOMIZED
p.legend.halign=PlotLegend.LEFT
p.legend.valign=PlotLegend.BOTTOM
p.legend.setLocation(0.8,4.85)
# p.legend.halign=PlotLegend.RIGHT
# p.legend.valign=PlotLegend.TOP
