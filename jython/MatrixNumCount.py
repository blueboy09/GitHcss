# MatrixMultiply Number Count

MatrixNumCount.MatrixGetALL()
#OptArray=["Bool1","Bool2","Byte1","Byte2","Short1","Short2","Int1","Int2","Long1","Long2","Float1","Float2","Double1","Double2"]
Path="C:\\Users\\yfjin\\hcss\\workresult\\Matrix\\"
OptArray=[MatrixNumCount.Bool1,MatrixNumCount.Bool2,MatrixNumCount.Byte1,MatrixNumCount.Byte2,\
	MatrixNumCount.Short1,MatrixNumCount.Short2,MatrixNumCount.Int1,MatrixNumCount.Int2,\
	MatrixNumCount.Long1,MatrixNumCount.Long2,MatrixNumCount.Float1,MatrixNumCount.Float2,\
	MatrixNumCount.Double1,MatrixNumCount.Double2]

for Opt in OptArray :
    MatrixNumCount.MatrixNcOutput(Opt,Opt._name,Path)
    MNumCount=MatrixNumCount.MatrixOptGetV(Opt)
    if(MNumCount > 0):
	MNumCount=MatrixNumCount.MatrixDimGet(Opt)
	MNumCount=Long2d(MNumCount)
	detail=MatrixNumCount.MatrixNcInput(Opt,Opt.get_name(),"C:\\Users\\yfjin\\hcss\\workresult\\Matrix\\")
	detail=Long2d(detail)

	p=PlotXY()
        p.plotSize=(4,4)
        p.gridLayout.vgap=0
        z_grid=Double1d(detail.get(1))
        p1_all= Double1d(detail.get(3))
        p1=SubPlot()
        p.addSubPlot(p1)
        p1L_all=LayerXY(z_grid, p1_all, name="the Matrix Multiply number",color=java.awt.Color.blue)
        p1L_all.style=Style(chartType=Style.HISTOGRAM_EDGE)
        p1L_all.xaxis=Axis(type=Axis.LINEAR, range=[0,3000])
        p1L_all.yaxis=Axis(range=[0,160000])
        p1L_all.xaxis.tick.setFixedValues(Double1d([0,500,1000,1500,2000,2500,3000]))
        p1L_all.xaxis.getTick().setLineWidth(1)
        p1L_all.xaxis.getTick().setHeight(0.05)
        #p1L_all.xaxis.tick.visible=0
        p1L_all.xaxis.tick.label.visible=1
        p1L_all.xaxis.title.visible=1
        p1L_all.xaxis.tick.label.fontSize=8
        p1L_all.xaxis.title.text="Matrix dimension"
        p1L_all.xaxis.title.fontSize=8
        p1L_all.yaxis.tick.label.fontSize=8
        p1L_all.yaxis.title.text="Number"
        p1L_all.yaxis.title.fontSize=8
        p1.addLayer(p1L_all)
        p1L_all.xaxis.auxAxes[0].tick.visible=0
        
        
        p.legend.visible=1
        p.legend.columns=1
        p.legend.position=PlotLegend.CUSTOMIZED
        p.legend.setLocation(1,4.0)
        p.legend.halign=PlotLegend.LEFT
        p.legend.valign=PlotLegend.BOTTOM
        p.legend.borderVisible = False
        #p.addAnnotation(Annotation(390,2500,"SVD",color=BLACK,fontSize=11))
        p.titleText="the detail count of MatrixMultiply"
        
#        p.close()
