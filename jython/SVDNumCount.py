# SVD Number Count
SVDNumCount.SVDGetALL()

Path="C:\\Users\\yfjin\\hcss\\workresult\\SVD\\"
SVDNumCount.SVDNcOutputALL(Path)
OptArray=[SVDNumCount.SVDF1,SVDNumCount.SVDF2,SVDNumCount.SVDD1,SVDNumCount.SVDD2]

for Opt in OptArray :
    svd=SVDNumCount.SVDGetCount(Opt)
    if(svd>0):
        svd=SVDNumCount.SVDNcInput(Opt,Path)
        svd=Long2d(svd)
        print "the number of SVD= ", svd
        
        p=PlotXY()
        p.plotSize=(4,4)
        p.gridLayout.vgap=0
        z_grid=Double1d(svd.get(0))
        p1_all= Double1d(svd.get(2))
        p1=SubPlot()
        p.addSubPlot(p1)
        p1L_all=LayerXY(z_grid, p1_all, name="the SVD number",color=java.awt.Color.blue)
        p1L_all.style=Style(chartType=Style.HISTOGRAM_EDGE)
        p1L_all.xaxis=Axis(type=Axis.LINEAR, range=[380,435])
        p1L_all.yaxis=Axis(range=[0,7000])
        p1L_all.xaxis.tick.setFixedValues(Double1d([390,400,410,420,430]))
        p1L_all.xaxis.getTick().setLineWidth(1)
        p1L_all.xaxis.getTick().setHeight(0.05)
        #p1L_all.xaxis.tick.visible=0
        p1L_all.xaxis.tick.label.visible=1
        p1L_all.xaxis.title.visible=1
        p1L_all.xaxis.tick.label.fontSize=8
        p1L_all.xaxis.title.text="SVD dimension"
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
        p.titleText="the detail count of SingularValueDecomposition"
        p.saveAsPNG(Path+"SVDfile.png") 
	p.saveAsEPS(Path+"SVDfile.eps") 
#        p.close()