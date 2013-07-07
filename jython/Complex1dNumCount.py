# the Complex1dNumCount Program analysis


OptArray=[Complex1dNumCount.Add1,Complex1dNumCount.Add2,Complex1dNumCount.Sub1,Complex1dNumCount.Sub2,\
	   Complex1dNumCount.Mul1,Complex1dNumCount.Mul2,Complex1dNumCount.Div1,Complex1dNumCount.Div2,\
	   Complex1dNumCount.Pow,Complex1dNumCount.Neg,Complex1dNumCount.Mod,Complex1dNumCount.Abs]

Path="C:\\Users\\yfjin\\hcss\\workresult\\Complex1d\\"
Complex1dNumCount.Complex1dNcOutputALL(Path)

for Opt in OptArray:
    s=Complex1dNumCount.Complex1dGetDtl(Opt)
    if(len(s[0])==0):
	continue
    ss=Complex1dNumCount.Complex1dGetDim(s)
    Array=Long1d(ss)
    Dim=len(Array)

    myPlot=PlotXY()
    myLayer1 = LayerXY(Double1d(range(Dim)),Double1d(Array),color=java.awt.Color.blue)
    myPlot.addLayer(myLayer1)
    myPlot.xaxis.type = Axis.LINEAR
    myPlot.yaxis.type = Axis.LOG
    myPlot.titleText = "Number Count of the Complex1d " + Opt.toString() + " Operation"
    myPlot.xaxis.titleText = "Array Scale of the Complex1d"
    myPlot.yaxis.titleText = "Number"
    myPlot.saveAsPNG(Path+Opt.toString()+"file.png") 
    myPlot.saveAsEPS(Path+Opt.toString()+"file.eps") 
    myPlot.close()
    