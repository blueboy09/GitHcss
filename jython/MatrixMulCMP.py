# the parameters to build the class MatrixMulCmp
begin=1
end=11
step=1
IterationNum=50
type=0 #means float
Path="C:\\Users\\yfjin\\hcss\\workresult\\Matrix\\"
ScaleMode=0 #log
CMP=MatrixMulCmp(begin,end,step,IterationNum,type)

timelist=CMP.MatrixMultime(ScaleMode)
Xd=range(begin,end,step)

myPlot = PlotXY()
myLayer1 = LayerXY(Double1d(Xd),Double1d(timelist[0]),color=java.awt.Color.red)
myLayer2 = LayerXY(Double1d(Xd),Double1d(timelist[1]),color=java.awt.Color.green)
myLayer1.line = Style.MARKED
myLayer2.line = Style.MARK_DASHED
myLayer1.name="float Matrixmultiply by pure java"
myLayer2.name="float Matrixmultiply by Jcublas"
myPlot.legend.visible = 1
myPlot.addLayer(myLayer1)
myPlot.addLayer(myLayer2)

type=1
timelist=CMP.MatrixMultime(ScaleMode)
myLayer3 = LayerXY(Double1d(Xd),Double1d(timelist[0]),color=java.awt.Color.blue)
myLayer4 = LayerXY(Double1d(Xd),Double1d(timelist[1]),color=java.awt.Color.black)
myLayer3.line = Style.MARKED
myLayer4.line = Style.MARK_DASHED
myLayer3.name="double Matrixmultiply by pure java "
myLayer4.name="double Matrixmultiply by Jcublas"
myPlot.legend.visible = 1
myPlot.addLayer(myLayer3)
myPlot.addLayer(myLayer4)

myPlot.xaxis.type = Axis.LINEAR
myPlot.yaxis.type = Axis.LOG
myPlot.titleText = "Comparison with CUDA and pure Java"
myPlot.subtitleText = "MatrixMultiply class(Double)"
myPlot.xaxis.titleText = "number of elements /log2(N)"
myPlot.yaxis.titleText = "Time"
myPlot.saveAsEPS(Path+ "cujaMatrixLog.eps") # Encapsulated PS

# rerun using the linear scale 

begin=1
end=221
step=10
IterationNum=50
type=0
Path="C:\\Users\\yfjin\\hcss\\workresult\\Matrix\\"
CMP.SetPara(begin,end,step,IterationNum,type)
ScaleMode=1

timelist=CMP.MatrixMultime(ScaleMode)
Xd=range(begin,end,step)

myPlot = PlotXY()
myLayer1 = LayerXY(Double1d(Xd),Double1d(timelist[0]),color=java.awt.Color.red)
myLayer2 = LayerXY(Double1d(Xd),Double1d(timelist[1]),color=java.awt.Color.green)
myLayer1.line = Style.MARKED
myLayer2.line = Style.MARK_DASHED
myLayer1.name="float Matrixmultiply by pure java "
myLayer2.name="float Matrixmultiply by Jcublas"
myPlot.legend.visible = 1
myPlot.addLayer(myLayer1)
myPlot.addLayer(myLayer2)


type=1
timelist=CMP.MatrixMultime(ScaleMode)
myLayer3 = LayerXY(Double1d(Xd),Double1d(timelist[0]),color=java.awt.Color.blue)
myLayer4 = LayerXY(Double1d(Xd),Double1d(timelist[1]),color=java.awt.Color.black)
myLayer3.line = Style.MARKED
myLayer4.line = Style.MARK_DASHED
myLayer3.name="double Matrixmultiply by pure java "
myLayer4.name="double Matrixmultiply by Jcublas"
myPlot.legend.visible = 1
myPlot.addLayer(myLayer3)
myPlot.addLayer(myLayer4)

#myPlot.xaxis.type = Axis.LOG
#myPlot.yaxis.type = Axis.LOG
myPlot.titleText = "Comparison with CUDA and pure Java"
myPlot.subtitleText = "MatrixMultiply class(Float/Double)"
myPlot.xaxis.titleText = "number of elements "
myPlot.yaxis.titleText = "time used"
myPlot.saveAsEPS(Path+"cujaMatrixLine.eps") 

