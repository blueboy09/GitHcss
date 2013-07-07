# the main Function  File

#///////////----------- import the sys file ---------------////////////////
import sys
sys.path.append("C:\\Users\\yfjin\\hcss\\workspace\\")
import time
import os
from herschel.ia.all import *

#///////////----------- execute the pipeline ---------------///////////////

path="C:\\Users\\yfjin\\hcss\\workspace\\"
pipeline="Photometer_Small_Map_Pipeline.py"
#pipelines=["Photometer_Small_Map_Pipeline",\
#	"Photometer_Parallel_Pipeline",\
#	"Photometer_Large_Map_Pipeline",\
#	"scanmap_Deep_Survey_miniscan_Pointsource"]

#for pipeline in pipelines:
# Reset the Counter
Double1dNumCount.ReSet()
Double2dNumCount.ReSet()
Complex1dNumCount.ReSet()
MatrixNumCount.ReSet()
FFTNumCount.ReSet()
SVDNumCount.ReSet()
beginPipeline=time.clock()

# execute the pipeline
execfile(path+pipeline+".py")

# output the results. the result output in the Dos Windows
endPipeline=time.clock()
TPipeline=endPipeline-beginPipeline
print TPipeline
Double1dNumCount.Double1dGetALL()
Double2dNumCount.Double2dGetALL()
Complex1dNumCount.Complex1dGetALL()
MatrixNumCount.MatrixGetALL()
FFTNumCount.FFTGetALL()
SVDNumCount.SVDGetALL()

# each method's number count
execfile(path+"Double1dNumCount.py")
execfile(path+"Complex1dNumCount.py")
execfile(path+"Double2dNumCount.py")
execfile(path+"FFTNumCount.py")
execfile(path+"SVDNumCount.py")
execfile(path+"MatrixNumCount.py")

# each meshod's time cost 
execfile(path+"Double1dFitTime.py")
execfile(path+"Complex1dFitTime.py")
execfile(path+"Double2dTimeCost.py")
execfile(path+"MatrixTimeCost.py")
execfile(path+"SVDTimeCost.py")
execfile(path+"FFTTimeCost.py")
