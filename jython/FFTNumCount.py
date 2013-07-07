# FFT number Count
Path="C:\\Users\\yfjin\\hcss\\workresult\\FFT\\"

FFTNumCount.FFTGetALL()
FFTNumCount.FFTNcOutputALL(Path)
OptArray=[FFTNumCount.NCfft,FFTNumCount.NCifft]

for Opt in OptArray:
    FNumCount=FFTNumCount.FFTGetCount(Opt)
    if(FNumCount == 0):
	break
    FFTGetD=Long1d(FFTNumCount.FFTGetDim(FFTNumCount.NCfft))
    Dim=len(FFTGetD)
    FFTPlot=PlotXY()
    FFTLayer1 = LayerXY(Double1d(range(Dim)),Double1d(FFTGetD),color=java.awt.Color.blue)
    FFTPlot.addLayer(FFTLayer1)
    FFTPlot.xaxis.type = Axis.LINEAR
    FFTPlot.yaxis.type = Axis.LOG
    FFTPlot.titleText = "Number Count of the Complex1d" + FFTNumCount.FFTtoString(Opt) + "Operation"
    FFTPlot.xaxis.titleText = "Array Scale"
    FFTPlot.yaxis.titleText = "number Count"
    FFTPlot.saveAsPNG(Path+ FFTNumCount.FFTtoString(Opt) +"file.png") 
    FFTPlot.saveAsEPS(Path+ FFTNumCount.FFTtoString(Opt) +"file.eps") 
    FFTPlot.close()
