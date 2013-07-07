# the main Function  File


#///////////-----------     preprocess      ----------------////////////////

# import the necessary module
import sys
import time
import os
from herschel.ia.all import *

# define the path of workspace
sys.path.append("C:\\Users\\yfjin\\hcss\\workspace\\")
path="C:\\Users\\yfjin\\hcss\\workspace\\"
#pipeline="Photometer_Small_Map_Pipeline"
pipeline="Spectrometer_Mapping_Pipeline"
#pipeline="Photometer_Large_Map_Pipeline"
#pipeline="scanmap_Deep_Survey_miniscan_Pointsource"
# Reset the Counter
Double1dNumCount.ReSet()
Double2dNumCount.ReSet()
Complex1dNumCount.ReSet()
MatrixNumCount.ReSet()
FFTNumCount.ReSet()
SVDNumCount.ReSet()
# start the stopwatcch
beginPipeline=time.clock()

#///////////----------- execute the pipeline ---------------///////////////

execfile(path+pipeline+".py")

#///////////-----------   post-processing   ---------------///////////////

# output the NumCount results. the result output in the Os-Console Windows

endPipeline=time.clock()
TPipeline=endPipeline-beginPipeline
print TPipeline
Double1dNumCount.Double1dGetALL()
Double2dNumCount.Double2dGetALL()
Complex1dNumCount.Complex1dGetALL()
MatrixNumCount.MatrixGetALL()
FFTNumCount.FFTGetALL()
SVDNumCount.SVDGetALL()

# execute the post-processing about NumCount.
# do something like draw the result and 
# output the result to memory
execfile(path+"FFTNumCount.py")
execfile(path+"Double1dNumCount.py")
execfile(path+"Complex1dNumCount.py")
#execfile(path+"Double2dNumCount.py")
execfile(path+"SVDNumCount.py")
execfile(path+"MatrixNumCount.py")

# execute the post-processing about TimeCost.
# each meshod's time cost 
execfile(path+"FFTTimeCost.py")
execfile(path+"Double1dFitTime.py")
execfile(path+"Complex1dFitTime.py")
#execfile(path+"Double2dTimeCost.py")
execfile(path+"MatrixTimeCost.py")
execfile(path+"SVDTimeCost.py")

 