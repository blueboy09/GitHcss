# the Double1dNumCount Program analysis

OptArray=[Double1dNumCount.Add1,Double1dNumCount.Add2,Double1dNumCount.Sub1,Double1dNumCount.Sub2,\
	   Double1dNumCount.Mul1,Double1dNumCount.Mul2,Double1dNumCount.Div1,Double1dNumCount.Div2,\
	   Double1dNumCount.Pow,Double1dNumCount.Neg,Double1dNumCount.Mod,Double1dNumCount.Abs,\
	   Double1dNumCount.DotProduct1,Double1dNumCount.DotProduct2,Double1dNumCount.OutProduct]

Path="C:\\Users\\yfjin\\hcss\\workresult\\Double1d\\"
Double1dNumCount.Double1dNcOutputALL(Path)

for Opt in OptArray:
    s=Double1dNumCount.Double1dGetDtl(Opt)
    if(len(s[0])==0):
	continue
    ss=Double1dNumCount.Double1dGetDim(s)
    Array=Long1d(ss)
    Dim=len(Array)

    myPlot=PlotXY()
    myLayer1 = LayerXY(Double1d(range(Dim)),Double1d(Array),color=java.awt.Color.blue)
    myPlot.addLayer(myLayer1)
    myPlot.titleText = "the Number Count of the Double1d " + Opt.toString() + " Operation"
    myPlot.xaxis.type = Axis.LINEAR
    myPlot.yaxis.type = Axis.LOG
    myPlot.xaxis.titleText = "Array Scale"
    myPlot.yaxis.titleText = "Number"
    myPlot.saveAsPNG(Path+Opt.toString()+"file.png") 
    myPlot.saveAsEPS(Path+Opt.toString()+"file.eps") 
    myPlot.close()
    