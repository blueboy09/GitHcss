# the Time Used Comparison about FFT and CudaFFT

begin = 1
end = 20
step = 1
IterationNum=50
Direction=-1
Path="C:\\Users\\yfjin\\hcss\\workresult\\FFT\\"
ScaleMode=0
CMP=FFTCmp(begin,end,step,IterationNum,Direction)
timelist=CMP.FFTtime(ScaleMode)
Xd=range(begin,end,step)

myPlot = PlotXY()
myLayer1 = LayerXY(Double1d(Xd),Double1d(timelist[0]),color=java.awt.Color.red)
myLayer2 = LayerXY(Double1d(Xd),Double1d(timelist[1]),color=java.awt.Color.green)
myLayer1.line = Style.MARKED
myLayer2.line = Style.MARK_DASHED
myLayer1.name="FFT by pure java"
myLayer2.name="FFT by Jcufft"
myPlot.legend.visible = 1
myPlot.addLayer(myLayer1)
myPlot.addLayer(myLayer2)

Direction=1
timelist=CMP.FFTtime(ScaleMode)
Xd=range(begin,end,step)

myLayer3 = LayerXY(Double1d(Xd),Double1d(timelist[0]),color=java.awt.Color.yellow)
myLayer4 = LayerXY(Double1d(Xd),Double1d(timelist[1]),color=java.awt.Color.blue)
myLayer3.line = Style.MARKED
myLayer4.line = Style.MARK_DASHED
myLayer3.name="IFFT by pure java"
myLayer4.name="IFFT by Jcufft"
myPlot.legend.visible = 1
myPlot.addLayer(myLayer3)
myPlot.addLayer(myLayer4)


myPlot.xaxis.type = Axis.LINEAR
myPlot.yaxis.type = Axis.LOG
myPlot.titleText = "Comparison with CUDA and pure Java"
myPlot.subtitleText = "FFT class(Double)"
myPlot.xaxis.titleText = "number of elements /log2(N)"
myPlot.yaxis.titleText = "Time"
myPlot.saveAsEPS(Path+"FFTCudaJava1.eps") # Encapsulated PS

## the linear rerun
begin=1
end=15001
step=1000
IterationNum=50
Direction=-1
Path="C:\\Users\\yfjin\\hcss\\workresult\\FFT\\"
CMP.SetPara(begin,end,step,IterationNum,Direction)
ScaleMode=1


timelist=CMP.FFTtime(ScaleMode)
Xd=range(begin,end,step)


myPlot = PlotXY()
myLayer1 = LayerXY(Double1d(Xd),Double1d(timelist[0]),color=java.awt.Color.red)
myLayer2 = LayerXY(Double1d(Xd),Double1d(timelist[1]),color=java.awt.Color.green)
myLayer1.line = Style.MARKED
myLayer2.line = Style.MARK_DASHED
myLayer1.name="FFT by pure java"
myLayer2.name="FFT by Jcufft"
myPlot.legend.visible = 1
myPlot.addLayer(myLayer1)
myPlot.addLayer(myLayer2)

Direction=1
timelist=CMP.FFTtime(ScaleMode)
Xd=range(begin,end,step)

myLayer3 = LayerXY(Double1d(Xd),Double1d(timelist[0]),color=java.awt.Color.yellow)
myLayer4 = LayerXY(Double1d(Xd),Double1d(timelist[1]),color=java.awt.Color.blue)
myLayer3.line = Style.MARKED
myLayer4.line = Style.MARK_DASHED
myLayer3.name="IFFT by pure java"
myLayer4.name="IFFT by Jcufft"
myPlot.legend.visible = 1
myPlot.addLayer(myLayer3)
myPlot.addLayer(myLayer4)


#myPlot.xaxis.type = Axis.LOG
#myPlot.yaxis.type = Axis.LOG
myPlot.titleText = "Comparison with CUDA and pure Java"
myPlot.subtitleText = "FFT class(Double)"
myPlot.xaxis.titleText = "number of elements "
myPlot.yaxis.titleText = "time used"
myPlot.saveAsEPS(Path+"FFTCudaJava2.eps") # Encapsula

