##def clip(ksigma,n,Xrg,Yrg,Wrg,mode):
##    myModel = PolynomialModel(mode)
##    myFitter = Fitter(Xrg, myModel)
##    fitresults = myFitter.fit(Yrg,Wrg)
##    Yrg1=myModel(Xrg)
##    Variance=0
##    N=0
##    for i in range(len(Xrg)):
##        if(Wrg[i]!=0):
##	    Variance=Variance+POW(ABS(Yrg[i]-Yrg1[i]),2)
##	    N=N+1
##    Variance=Variance/N
##    Sigma=SQRT(Variance)
##    
##    if ABS(Yrg[n]-Yrg1[n]) > ksigma*Sigma:
##        return 0
##    else:
##        return 1
##
##
##def cliper(ksigma,X,Y,W,mode):
##    lenX=len(X)
##    for i in range(5):
##	rg=Range(i,i+10)
##	Xrg=X.get(rg)
##	Yrg=Y.get(rg)
##	Wrg=W.get(rg)
##	Wrg.set(0,0)
##	W[i]=clip(ksigma,0,Xrg,Yrg,Wrg,mode)
##    for i in range(5,lenX-5):
##	rg=Range(i-5,i+5)
##	Xrg=X.get(rg)
##	Yrg=Y.get(rg)
##	Wrg=W.get(rg)
##	Wrg.set(5,0)
##	W[i]=clip(ksigma,5,Xrg,Yrg,Wrg,mode)
##    for i in range(lenX-5,lenX):
##	rg=Range(i-10,i)
##	Xrg=X.get(rg)
##	Yrg=Y.get(rg)
##	Wrg=W.get(rg)
##	Wrg.set(9,0)
##	W[i]=clip(ksigma,9,Xrg,Yrg,Wrg,mode)
##    return W
##
### the function fittime Used for fitting the time curve
##def fitTime(Opt,Nout,Nin,begin,end,step,mode):
##    OptTimeCost=Double1dTimeCost(Opt,Nout,Nin,begin,end,step)
##    Y=OptTimeCost.Double1dTimeTest(Opt)
##    Y=Double1d(Y)
##    X=Double1d(range(begin,end,step))
##    myModel = PolynomialModel(mode)
##    myFitter = Fitter(X, myModel)
##    # result 1
##    fitresults1 = myFitter.fit(Y)
##    
##    myPlot = PlotXY()
##    myLayer1 = LayerXY(Double1d(X),Double1d(Y),color=java.awt.Color.blue)
##    myLayer1.name="the real time cost curve of " +Opt
##    myLayer2 = LayerXY(Double1d(X),myModel(X),color=java.awt.Color.red)
##    myLayer2.name="the fit curve of time cost of " +Opt
##    myPlot.addLayer(myLayer1)
##    myPlot.addLayer(myLayer2)
##    myPlot.legend.visible =1
##    myPlot.titleText = "the Time Used of the Double1d " + Opt +"Operation"
##    myPlot.xaxis.titleText = "The number of elements in one dimension"
##    myPlot.yaxis.titleText = "The time cost"
##
##    W=[]
##    lenX=len(X)
##    for i in range(lenX):
##	W.append(1)
##    W=Double1d(W)
##    W=cliper(3,X,Y,W,mode)
##    W=Double1d(W) 
##    yWeight=cliper(5,X,Y,W,mode)
##
##    yWeights=Double1d(yWeight) 
##    #print yWeights 
##    fitresults2 = myFitter.fit(Y, yWeights)
##    
##    myLayer3 = LayerXY(Double1d(X),myModel(X),color=java.awt.Color.green)
##    myLayer3.name="the fit curve without singular point "+Opt
##    myPlot.addLayer(myLayer3)
##    myPlot.saveAsPNG(Path+Opt+"JavaTime.png")
##    return myModel
##
##
### the function TimeUsed Used for input the CountData and calculate each Opearator's time cost
##def TimeUsed(Opt,Path,Nout,Nin,begin,end,step,mode):
##    DataAdd1=Double1dTimeCost.Double1dInput(Opt,Path)
##    Add1Model=fitTime(Opt,Nout,Nin,begin,end,step,mode)
##    theTimeUsed=0
##    Dim=Double1dNumCount.GetDimValue()
##    ss=Double1d(range(Dim))
##    X=Add1Model(ss)
##    Y=Long1d(DataAdd1)
##    Y=Double1d(Y)
##    for i in range(Dim):
##        theTimeUsed=theTimeUsed+Y[i]*X[i]
##    return theTimeUsed
##
##
##Opt="Add1"
##Path="C:\\Users\\yfjin\\hcss\\workresult\\Double1d\\"
##Nout=10
##Nin=10
##begin=1
##end=10001
##step=500
##
##
##SmallPipelineTimeUsed={"Add1":0,"Add2":0,"Sub1":0,"Sub2":0,"Mul1":0,"Mul2":0,"Div1":0,"Div2":0,"Pow":0,"Neg":0,"Abs":0,"Mod":0,"Get":0,"Set":0,"DotProduct1":0,"DotProduct2":0,"OutProduct":0}
##Operation=["Add1","Add2","Sub1","Sub2","Mul1","Mul2","Div1","Div2","Pow","Neg","Abs","Mod","Get","Set","DotProduct1"]
##mode=1
##SPTimeUsed=[]
##AllTime=0
##for Opt in Operation:
##    OptTimeUsed=TimeUsed(Opt,Path,Nout,Nin,begin,end,step,mode)
##    AllTime=AllTime+OptTimeUsed
##    SPTimeUsed.append(OptTimeUsed)
##    SmallPipelineTimeUsed[Opt]=OptTimeUsed
##
##Operation=["OutProduct","DotProduct2"]
##mode=2
##for Opt in Operation:
##    OptTimeUsed=TimeUsed(Opt,Path,Nout,Nin,begin,end,step,mode)
##    AllTime=AllTime+OptTimeUsed
##    SPTimeUsed.append(OptTimeUsed)
##    SmallPipelineTimeUsed[Opt]=OptTimeUsed
##
##
##myPlot = PlotXY()
##myLayer1 = LayerXY(Double1d(range(len(Operation))),Double1d(SPTimeUsed),color=java.awt.Color.blue)
##myLayer1.name="the real time used of small map pipeline" 
##myPlot.addLayer(myLayer1)
##myPlot.legend.visible =0
##myPlot.titleText = "the real time used of small map pipeline" 
##myPlot.xaxis.titleText = "The Variety of the Calculate Operation"
##myPlot.yaxis.titleText = "The Time Used"
##myPlot.saveAsPNG(Path+"AllOptTime.png")
#
## A plot with different panels
#
## Set up some dummy data to plot
#freq = Double1d(range(500, 1600, 10))
#line = EXP(-(freq-1000)**2/30.0**2) + RandomUniform(0.1)(freq)-0.05
#lineStrength = [0.5, 0.2, 0.4, 0.3, 0.7, 0.9]
#
## Initialise the plot
#p = PlotXY()
## Specify the plot dimensions on the screen
#p.plotSize=(2,2)
## Set the positions for the subplots in a grid layout
#topLeft     = SubPlot(SubPlotGridConstraints(0,0))
#bottomLeft  = SubPlot(SubPlotGridConstraints(0,1))
#topMid      = SubPlot(SubPlotGridConstraints(1,0))
#bottomMid   = SubPlot(SubPlotGridConstraints(1,1))
#topRight    = SubPlot(SubPlotGridConstraints(2,0))
#bottomRight = SubPlot(SubPlotGridConstraints(2,1))
## Fill the sub-plots
#Layer= LayerXY(freq, lineStrength[0]*line, color=java.awt.Color.BLACK,stroke=1.5, chartType=Style.HISTOGRAM)
#bottomLeft.addLayer(Layer)
#bottomMid.addLayer(LayerXY(freq, lineStrength[1]*line, color=java.awt.Color.GRAY, \
#   stroke=1, chartType=Style.HISTOGRAM))
#bottomRight.addLayer(LayerXY(freq, lineStrength[2]*line, color=java.awt.Color.BLACK, \
#   stroke=1, chartType=Style.HISTOGRAM))
#topLeft.addLayer(LayerXY(freq, lineStrength[3]*line, color=java.awt.Color.BLACK, \
#   stroke=1, chartType=Style.HISTOGRAM))
#topMid.addLayer(LayerXY(freq, lineStrength[4]*line, color=java.awt.Color.GRAY, \
#   stroke=1, chartType=Style.HISTOGRAM))
#topRight.addLayer(LayerXY(freq, lineStrength[5]*line, color=java.awt.Color.BLACK, \
#   stroke=1, chartType=Style.HISTOGRAM))
##
## Set the tick label and ranges for each subplot, and add it to the main plot
#for subP in [topLeft, topRight, bottomLeft, bottomRight, topMid, bottomMid]:
#   # Remove all axes labels to start with (add needed ones later)
#   subP.baseLayerXY.xaxis.tick.labelVisible = 0
#   subP.baseLayerXY.xaxis.title.visible = 0
#   subP.baseLayerXY.yaxis.tick.labelVisible = 0
#   subP.baseLayerXY.yaxis.title.visible = 0
#   # Set axis ranges to be the same for all sub-plots
#   subP.baseLayerXY.xaxis.range = [400.0, 1600.0]
#   subP.baseLayerXY.yaxis.range = [-0.1, 1.1]
#   # Set the ticks for the xaxis to be at nice intervals
#   subP.baseLayerXY.xaxis.tick.setFixedValues(Double1d([500, 1000, 1500]), \
#      Double1d(range(400, 1600, 100)))
#   p.addSubPlot(subP)
## Set the gap between the sub-plots to be zero (i.e. plots touching each other)
##p.gridLayout.setGap(0, 0)
##
### Set the titles for the left hand axes of left hand plots
### and make the tick labels visible on these axes
##topLeft.baseLayerXY.yaxis.title.visible = 1
##topLeft.baseLayerXY.yaxis.titleText = "Flux Density"
##topLeft.baseLayerXY.yaxis.tick.labelVisible = 1
##bottomLeft.baseLayerXY.yaxis.title.visible = 1
##bottomLeft.baseLayerXY.yaxis.titleText = "Flux Density"
##bottomLeft.baseLayerXY.yaxis.tick.labelVisible = 1
### Make the tick labels visible on the lower xaxis
##bottomLeft.baseLayerXY.xaxis.tick.labelVisible = 1
##bottomMid.baseLayerXY.xaxis.tick.labelVisible = 1
##bottomRight.baseLayerXY.xaxis.tick.labelVisible = 1
### Use the upper xaxis for a title for each column
##topLeft.baseLayerXY.xaxis.getAuxAxis(0).titleText = "CRL 618"
##topLeft.baseLayerXY.xaxis.getAuxAxis(0).title.visible = 1
##topMid.baseLayerXY.xaxis.getAuxAxis(0).titleText = "M83"
##topMid.baseLayerXY.xaxis.getAuxAxis(0).title.visible = 1
##topRight.baseLayerXY.xaxis.getAuxAxis(0).titleText = "Orion Bar"
##topRight.baseLayerXY.xaxis.getAuxAxis(0).title.visible = 1
### Set some annotations
##topLeft.baseLayerXY.setAnnotation(1, Annotation(500, 0.9, "(a)", fontSize=14))
##topMid.baseLayerXY.setAnnotation(1, Annotation(500, 0.9, "(b)", fontSize=14))
##topRight.baseLayerXY.setAnnotation(1, Annotation(500, 0.9, "(c)", fontSize=14))
##bottomLeft.baseLayerXY.setAnnotation(1, Annotation(500, 0.9, "(d)", fontSize=14))
##bottomMid.baseLayerXY.setAnnotation(1, Annotation(500, 0.9, "(e)", fontSize=14))
##bottomRight.baseLayerXY.setAnnotation(1, Annotation(500, 0.9, "(f)", fontSize=14))
### Use the plot subtitle to contain a single label for all 3 x-axes
##p.subtitle.text = "Frequency (GHz)"
##p.subtitle.fontSize = p.title.fontSize
##from herschel.ia.gui.plot import PlotTitle
##p.subtitle.position = PlotTitle.BOTTOMCENTER
#from java.awt.geom import Point2D
#from java.awt.Color import *
#from herschel.ia.gui.plot import PlotLegend
#
## SubPlot Main
#sll=LayerXY(Double1d(0), Double1d(0))
#sll.xaxis=Axis(type=Axis.LOG, range=[10,2000000], titleText="wavelength $\\mathrm{\\lambda}$ [$\\mathrm{\\micro}$m]")
#sll.xaxis.title.fontSize=10
#sll.yaxis=Axis(type=Axis.LOG, range=[0.05,1000], titleText="flux density [Jy]")
#sll.yaxis.title.fontSize=10
#sll.inLegend=0
#sp0=SubPlot(SubPlotGridConstraints(0,0))
#sp0.addLayer(sll)
#p=PlotXY()
#p.addSubPlot(sp0)
#p.legend.visible=1
#
## Xilouris et al. 2004
#xx=Double1d([15])
#xy=Double1d([0.11])
#xyel=Double1d([0.02])
#xyeh=Double1d([0.02])
#xl=LayerXY(xx,xy)
#xl.errorY=[xyel,xyeh]
#xl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.SQUARE, symbolSize=6)
#xl.name="Xilouris et al. 2004"
#sp0.addLayer(xl)
#
## Golombek et al. 1988
#gx=Double1d([24,60,100])
#gy=Double1d([0.18,0.52,0.52])
#gyel=Double1d([0.04,0.09,0.09])
#gyeh=Double1d([0.04,0.09,0.09])
#gl=LayerXY(gx,gy)
#gl.errorY=[gyel,gyeh]
#gl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.FTRIANGLE, symbolSize=7)
#gl.name="Golombek et al. 1988"
#sp0.addLayer(gl)
#
##Shi et al. 2007
#sx=Double1d([23,70,150])
#sy=Double1d([0.17,0.44,0.6])
#sl=LayerXY(sx,sy)
#sl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.FDIAMOND, symbolSize=7)
#sl.name="Shi et al. 2007"
#sp0.addLayer(sl)
#
## Haas et al. 2004
#hx=Double1d([440,830])
#hy=Double1d([1.3,2.3])
#hyel=Double1d([0.4,0.5])
#hyeh=Double1d([0.4,0.5])
#hl=LayerXY(hx,hy)
#hl.errorY=[hyel,hyeh]
#hl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.TRIANGLE, symbolSize=7)
#hl.name="Haas et al. 2004"
#sp0.addLayer(hl)
#
## Wright et al. 2009
#wx=Double1d([3200,5000,7400,9000,12000])
#wy=Double1d([5.6,9,12,14,17])
#wl=LayerXY(wx,wy)
#wl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.STAR, symbolSize=7)
#wl.name="Wright et al. 2009"
#sp0.addLayer(wl)
#
## Cotton et al. 2009
#cx=Double1d([3200,20000,45000,60000,180000,900000])
#cy=Double1d([8,24,46,56,120,260])
#cl=LayerXY(cx,cy)
#cl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.FOCTAGON, symbolSize=7)
#cl.name="Cotton et al. 2009"
#sp0.addLayer(cl)
#
## This work
#tx=Double1d([100,150,240,340,500])
#ty=Double1d([0.5,0.66,0.8,1.06,1.4])
#tyel=Double1d([0.12,0.16,0.22,0.26,0.36])
#tyeh=Double1d([0.12,0.16,0.22,0.26,0.36])
#tl=LayerXY(tx,ty)
#tl.errorY=[tyel,tyeh]
#tl.style=Style(line=0, color=RED, symbolShape=SymbolShape.FOCTAGON, symbolSize=7)
#tl.name="This Work"
#sp0.addLayer(tl)
#
## Fit solid line
#slx=Double1d([10, 2000000])
#sly=Double1d([0.09, 900])
#sl1=LayerXY(slx,sly)
#sl1.style=Style(line=1, color=BLUE)
#sl1.inLegend=0
#sp0.addLayer(sl1)
#
## Fit dashed line
#dlx=Double1d([10, 2000000])
#dly=Double1d([0.1, 820])
#dll=LayerXY(dlx,dly)
#dll.style=Style(line=3, color=BLUE, dashArray=[3,3])
#dll.inLegend=0
#sp0.addLayer(dll)
#
## Display legends
#p.legend.visible=1
#p.legend.columns=1
#p.legend.position=PlotLegend.CUSTOMIZED
#p.legend.halign=PlotLegend.LEFT
#p.legend.valign=PlotLegend.BOTTOM
#p.legend.setLocation(0.8,4.85)
## p.legend.halign=PlotLegend.RIGHT
## p.legend.valign=PlotLegend.TOP
#
## subplot residual
#spr=SubPlot(SubPlotGridConstraints(0,1,1,0.5))
#slrl=LayerXY(Double1d(0), Double1d(0))
#slrl.inLegend=0
#slrl.xaxis=Axis(type=Axis.LOG, range=[10,1000], titleText="wavelength $\\mathrm{\\lambda}$ [$\\mathrm{\\micro}$m]")
#slrl.xaxis.title.fontSize=10
#slrl.yaxis=Axis(type=Axis.LINEAR, range=[-0.7, 0.7], titleText="residual [Jy]")
#slrl.yaxis.title.fontSize=10
#spr.addLayer(slrl)
#p.addSubPlot(spr)
#
## Xilouris et al. 2004 R
#spr1=SubPlot(SubPlotGridConstraints(1,1,1,1.5))
#xry=Double1d([-0.01])
#xrl=LayerXY(xx,xry)
#xrl.errorY=[xyel,xyeh]
#xrl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.SQUARE, symbolSize=6)
#xrl.inLegend=0
#xrl.name="Xilouris et al. 2004 R"
#spr1.addLayer(xrl)
#p.addSubPlot(spr1)
#
## Golombek et al. 1988 R
#gry=Double1d([0.01,0.2,0.06])
#grl=LayerXY(gx,gry)
#grl.errorY=[gyel,gyeh]
#grl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.FTRIANGLE, symbolSize=7)
#grl.inLegend=0
#grl.name="Golombek et al. 1988 R"
#spr.addLayer(grl)
#
## Shi et al. 2007 R
#sry=Double1d([0.0,0.07,-0.11])
#srl=LayerXY(sx,sry)
#srl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.FDIAMOND, symbolSize=7)
#srl.inLegend=0
#srl.name="Shi et al. 2007 R"
#spr.addLayer(srl)
#
## Haas et al. 2004
#hry=Double1d([-0.23,-0.03])
#hrl=LayerXY(hx,hry)
#hrl.errorY=[hyel,hyeh]
#hrl.style=Style(line=0, color=BLUE, symbolShape=SymbolShape.TRIANGLE, symbolSize=7)
#hrl.inLegend=0
#hrl.name="Haas et al. 2004"
#spr.addLayer(hrl)
#
## This work
#trry=Double1d([0.01,-0.03,-0.13,-0.21,-0.26])
#trl=LayerXY(tx,trry)
#trl.errorY=[tyel,tyeh]
#trl.style=Style(line=0, color=RED, symbolShape=SymbolShape.FOCTAGON, symbolSize=7)
#trl.inLegend=0
#trl.name="This Work"
#spr.addLayer(trl)
#
#
## Fit solid line
#slrx=Double1d([10,1000])
#slry=Double1d([0,0])
#slrl=LayerXY(slrx,slry)
#slrl.style=Style(line=1, color=BLUE)
#slrl.inLegend=0
#spr.addLayer(slrl)

#
#Add1TCPlot=PlotXY()
#Add1TCPlot.plotSize=(1,0)
#topLeft     = SubPlot(SubPlotGridConstraints(0,0))
#topMid      = SubPlot(SubPlotGridConstraints(0,1,1,0.6))
#Add1TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListAdd1),color=java.awt.Color.red)
##Add1TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListAdd1Once),color=java.awt.Color.blue)
#Add1TCLayer3 = LayerXY(Double1d(std),Double1d(TimeListAdd1WithoutFor),color=java.awt.Color.green)
#Add1TCLayer4 = LayerXY(Double1d(std),Double1d(TimeListAdd1OnceJava),color=java.awt.Color.orange)
#Add1TCLayer6 = LayerXY(Double1d(std),Double1d(TimeListAdd1OnceJava),color=java.awt.Color.orange)
#Add1TCLayer5 = LayerXY(Double1d(std),Double1d(TimeListFor),color=java.awt.Color.magenta)
#topLeft.addLayer(Add1TCLayer1)
##Add1TCPlot.addLayer(Add1TCLayer2)
##topLeft.addLayer(Add1TCLayer3)
##topLeft.addLayer(Add1TCLayer4)
#topLeft.addLayer(Add1TCLayer5)
##topMid.addLayer(Add1TCLayer6)
#topMid.addLayer(Add1TCLayer3)
#Add1TCPlot.addSubPlot(topLeft)
#Add1TCPlot.addSubPlot(topMid)
#
#Add1TCLayer1.name="time cost of jython time.clock()"
##Add1TCLayer2.name="one time calculate"
#Add1TCLayer3.name="time cost of jython time.clock minus empty 'for' loop cost"
##Add1TCLayer4.name="time cost by java System.nanoTime() "
#Add1TCLayer5.name="time cost of the empty 'for' loop "
##Add1TCLayer6.name="time cost by java System.nanoTime()"
#Add1TCPlot.legend.visible = 1
#
#Add1TCPlot.titleText = "Time Cost of Function in jython environment"
#Add1TCPlot.subtitleText = "by the Double1d add operator"
#topLeft.baseLayerXY.yaxis.titleText = "timecost"
#topLeft.baseLayerXY.xaxis.title.visible = 0
#topLeft.baseLayerXY.xaxis.titleText = "data scale"
#topMid.baseLayerXY.yaxis.titleText = "timecost"
#topMid.baseLayerXY.xaxis.titleText = "data scale"
#
#Add1TCPlot.legend.visible=1	
#Add1TCPlot.legend.columns=1
#Add1TCPlot.legend.position=PlotLegend.CUSTOMIZED
#Add1TCPlot.legend.halign=PlotLegend.LEFT
#Add1TCPlot.legend.valign=PlotLegend.BOTTOM
#Add1TCPlot.legend.setLocation(0.8,4.85)


Add1TCPlot=PlotXY()
Add1TCPlot.setLayout(PlotOverlayLayout())
topLeft     = SubPlot(SubPlotGridConstraints(0,0))
topMid      = SubPlot(SubPlotGridConstraints(0,1,1,0.6))
Add1TCLayer1 = LayerXY(Double1d(std),Double1d(TimeListAdd1),color=java.awt.Color.red)
#Add1TCLayer2 = LayerXY(Double1d(std),Double1d(TimeListAdd1Once),color=java.awt.Color.blue)
Add1TCLayer3 = LayerXY(Double1d(std),Double1d(TimeListAdd1WithoutFor),color=java.awt.Color.green)
Add1TCLayer4 = LayerXY(Double1d(std),Double1d(TimeListAdd1OnceJava),color=java.awt.Color.orange)
Add1TCLayer6 = LayerXY(Double1d(std),Double1d(TimeListAdd1OnceJava),color=java.awt.Color.red)
Add1TCLayer5 = LayerXY(Double1d(std),Double1d(TimeListFor),color=java.awt.Color.magenta)
#topLeft.addLayer(Add1TCLayer1)
Add1TCPlot.addLayer(Add1TCLayer3)
Add1TCPlot.addLayer(Add1TCLayer4)
#topLeft.addLayer(Add1TCLayer3)
#topLeft.addLayer(Add1TCLayer4)
#topLeft.addLayer(Add1TCLayer5)
#topMid.addLayer(Add1TCLayer6)
#topMid.addLayer(Add1TCLayer3)
#Add1TCPlot.addSubPlot(topLeft)
#Add1TCPlot.addSubPlot(topMid)



#Add1TCLayer1.name="time cost of jython time.clock()"
#Add1TCLayer2.name="one time calculate"
Add1TCLayer3.name="time cost of jython time.clock minus empty 'for' loop cost"
Add1TCLayer4.name="time cost by java System.nanoTime() "
#Add1TCLayer5.name="time cost of the empty 'for' loop "
Add1TCLayer6.name="detail draw of time cost of java"
Add1TCPlot.legend.visible = 1

mySubplot = SubPlot(SubPlotBoundsConstraints(0.05, 0.2, 0.75, 0.5))
# You add layers to a subplot in the same way as to a plot.
mySubplot.addLayer(Add1TCLayer6)
Add1TCPlot.addSubPlot(mySubplot)
mySubplot.baseLayerXY.xaxis.range = [0, 1500]
mySubplot.baseLayerXY.yaxis.range = [-0.0000001, 0.000002]
Add1TCPlot.titleText = "Difference time cost of the jython and java "
Add1TCPlot.subtitleText = "by the Double1d add operator"

#topLeft.baseLayerXY.yaxis.titleText = "timecost"
#topLeft.baseLayerXY.xaxis.title.visible = 0
#topLeft.baseLayerXY.xaxis.titleText = "data scale"
#topMid.baseLayerXY.yaxis.titleText = "timecost"
#topMid.baseLayerXY.xaxis.titleText = "data scale"
Add1TCPlot.xaxis.titleText = "data scale"
Add1TCPlot.yaxis.titleText = "time cost"
mySubplot.baseLayerXY.xaxis.title.visible = 0
mySubplot.baseLayerXY.yaxis.title.visible = 0

#Add1TCPlot.legend.visible=1	
#Add1TCPlot.legend.columns=1
#Add1TCPlot.legend.position=PlotLegend.CUSTOMIZED
#Add1TCPlot.legend.halign=PlotLegend.LEFT
#Add1TCPlot.legend.valign=PlotLegend.BOTTOM
#Add1TCPlot.legend.setLocation(0.8,4.85)