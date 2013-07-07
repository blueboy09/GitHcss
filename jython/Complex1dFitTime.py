# fit the time curve
# the function clip Used for clear the strange point
# fit the time curve
# the function clip Used for clear the strange point
def clip(ksigma,n,Xrg,Yrg,Wrg):
    myModel = PolynomialModel(1)
    myFitter = Fitter(Xrg, myModel)
    fitresults = myFitter.fit(Yrg,Wrg)
    Yrg1=myModel(Xrg)
    Variance=0
    N=0
    for i in range(len(Xrg)):
        if(Wrg[i]!=0):
	    Variance=Variance+POW(ABS(Yrg[i]-Yrg1[i]),2)
	    N=N+1
    Variance=Variance/N
    Sigma=SQRT(Variance)
    
    if ABS(Yrg[n]-Yrg1[n]) > ksigma*Sigma:
        return 0
    else:
        return 1


def cliper(ksigma,X,Y,W):
    lenX=len(X)
    for i in range(5):
	rg=Range(i,i+10)
	Xrg=X.get(rg)
	Yrg=Y.get(rg)
	Wrg=W.get(rg)
	Wrg.set(0,0)
	W[i]=clip(ksigma,0,Xrg,Yrg,Wrg)
    for i in range(5,lenX-5):
	rg=Range(i-5,i+5)
	Xrg=X.get(rg)
	Yrg=Y.get(rg)
	Wrg=W.get(rg)
	Wrg.set(5,0)
	W[i]=clip(ksigma,5,Xrg,Yrg,Wrg)
    for i in range(lenX-5,lenX):
	rg=Range(i-10,i)
	Xrg=X.get(rg)
	Yrg=Y.get(rg)
	Wrg=W.get(rg)
	Wrg.set(9,0)
	W[i]=clip(ksigma,9,Xrg,Yrg,Wrg)
    return W

# the function fittime Used for fitting the time curve
def fitTime(Opt,begin,end,step):
    Y=[]
    for i in range(begin,end,step):
	Y.append(Complex1dTimeCost.TimeCal(Opt,i))
    Y=Double1d(Y)
    X=Double1d(range(begin,end,step))
    myModel = PolynomialModel(1)
    myFitter = Fitter(X, myModel)
    # result 1
    fitresults1 = myFitter.fit(Y)
    
    myPlot = PlotXY()
    myLayer1 = LayerXY(Double1d(X),Double1d(Y),color=java.awt.Color.blue)
    myLayer1.name="real time cost curve of " +Opt
    myLayer2 = LayerXY(Double1d(X),myModel(X),color=java.awt.Color.red)
    myLayer2.name="fit curve of time cost of " +Opt
    myPlot.addLayer(myLayer1)
    myPlot.addLayer(myLayer2)
    myPlot.legend.visible =1
    myPlot.titleText = "Time Used of the Complex1d " + Opt +"Operation"
    myPlot.xaxis.titleText = "The number of elements in one dimension"
    myPlot.yaxis.titleText = "The time cost"

    W=[]
    lenX=len(X)
    for i in range(lenX):
	W.append(1)
    W=Double1d(W)
    W=cliper(5,X,Y,W)
    W=Double1d(W) 
    yWeight=cliper(3,X,Y,W)

    yWeights=Double1d(yWeight) 
    #print yWeights 
    fitresults2 = myFitter.fit(Y, yWeights)
    
    myLayer3 = LayerXY(Double1d(X),myModel(X),color=java.awt.Color.green)
    myLayer3.name="fit curve without singular point "+Opt
    myPlot.addLayer(myLayer3)
    myPlot.saveAsPNG(Path+Opt+"JavaTime.png")
    myPlot.close()
    return myModel


# the function TimeUsed Used for input the CountData and calculate each Opearator's time cost
def TimeUsed(Opt,Path,begin,end,step):
    theTimeUsed=0

    myData=Complex1dTimeCost.TcInput(Opt,Path)
    if(len(myData[0])==0):
	return 0
    myData=Long2d(myData)
    nums=myData.getDimension(1)
    rg=Range(0,nums)
    myData1=myData.get(0,rg)
    myData2=myData.get(1,rg)
    Dim=myData.get(0,nums-1)
    ss=Double1d(range(Dim+1))
    myModel=fitTime(Opt,begin,end,step)
    X=myModel(ss)

    myData2=Double1d(myData2)
    for i in range(nums):
	j=myData1[i]
        theTimeUsed=theTimeUsed+X[j]*myData2[i]
    return theTimeUsed



Path="C:\\Users\\yfjin\\hcss\\workresult\\Complex1d\\"
begin=1
end=20001
step=500


SmallPipelineTimeUsed={"Add1":0,"Add2":0,"Sub1":0,"Sub2":0,"Mul1":0,"Mul2":0,"Div1":0,"Div2":0,"Pow":0,"Neg":0,"Abs":0,"Mod":0}
Operation=["Add1","Add2","Sub1","Sub2","Mul1","Mul2","Div1","Div2","Pow","Neg","Abs","Mod"]
OptArray=[Complex1dNumCount.Add1,Complex1dNumCount.Add2,Complex1dNumCount.Sub1,Complex1dNumCount.Sub2,\
	   Complex1dNumCount.Mul1,Complex1dNumCount.Mul2,Complex1dNumCount.Div1,Complex1dNumCount.Div2,\
	   Complex1dNumCount.Pow,Complex1dNumCount.Neg,Complex1dNumCount.Mod,Complex1dNumCount.Abs]

SPTimeUsed=[]
AllTime=0
for Opt in Operation:
    OptTimeUsed=TimeUsed(Opt,Path,begin,end,step)
    AllTime=AllTime+OptTimeUsed
    SPTimeUsed.append(OptTimeUsed)
    SmallPipelineTimeUsed[Opt]=OptTimeUsed

print SmallPipelineTimeUsed
fp = open(Path+"result.txt",'w')
print >> fp, SmallPipelineTimeUsed
fp.close()

myPlot = PlotXY()
myLayer1 = LayerXY(Double1d(range(len(Operation))),Double1d(SPTimeUsed),color=java.awt.Color.blue)
myLayer1.name="real time used of small map pipeline" 
myPlot.addLayer(myLayer1)
myPlot.legend.visible =0
myPlot.titleText = "real time used of small map pipeline" 
myPlot.xaxis.titleText = "Variety of the Calculate Operation"
myPlot.yaxis.titleText = "Time Used"
myPlot.saveAsPNG(Path+"AllOptTime.png")
myPlot.saveAsEPS(Path+"AllOptTime.eps")
#myPlot.close()

