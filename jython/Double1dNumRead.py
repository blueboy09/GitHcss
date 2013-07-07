# Double1d Number Read
Path="C:\\Users\\yfjin\\hcss\\workresult\\Double1d\\"
OptArray=[Double1dNumCount.Add1,Double1dNumCount.Add2,Double1dNumCount.Sub1,Double1dNumCount.Sub2,\
	   Double1dNumCount.Mul1,Double1dNumCount.Mul2,Double1dNumCount.Div1,Double1dNumCount.Div2,\
	   Double1dNumCount.Pow,Double1dNumCount.Abs,Double1dNumCount.Mod,Double1dNumCount.Neg,\
	   Double1dNumCount.DotProduct1,Double1dNumCount.DotProduct2,Double1dNumCount.OutProduct]
for Opt in OptArray:
    OptNums=Double1dNumCount.Double1dNcInput(Opt,Path)
    if(len(OptNums[0])==0):
	continue
    OptNumber=Double1dNumCount.Double1dGetDim(OptNums)
    OptNumber=Long1d(OptNumber)
    OptPlot=PlotXY()
    Dim=OptNumber.length()
    OptLayer1 = LayerXY(Double1d(range(Dim)),Double1d(OptNumber),color=java.awt.Color.blue)
    OptPlot.addLayer(OptLayer1)
    OptPlot.xaxis.type = Axis.LINEAR
    OptPlot.yaxis.type = Axis.LOG
    OptPlot.titleText = "the Number Count of the Double1d "+ Opt.toString()+ " Operation"
    OptPlot.xaxis.titleText = "Array Scale"
    OptPlot.yaxis.titleText = "number"
    OptPlot.saveAsPNG("C:\\Users\\yfjin\\hcss\\workresult\\Double1d\\" + Opt.toString()+ "file.png") 
    OptPlot.saveAsEPS("C:\\Users\\yfjin\\hcss\\workresult\\Double1d\\" + Opt.toString()+ "file.eps") 
    OptPlot.close()