Double1dNumCount.ReSet()
Double2dNumCount.ReSet()
Complex1dNumCount.ReSet()
MatrixNumCount.ReSet()
FFTNumCount.ReSet()
SVDNumCount.ReSet()
import time
beginPipeline=time.clock()


# 
#  This file is part of Herschel Common Science System (HCSS).
#  Copyright 2001-2012 Herschel Science Ground Segment Consortium
# 
#  HCSS is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as
#  published by the Free Software Foundation, either version 3 of
#  the License, or (at your option) any later version.
# 
#  HCSS is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
# 
#  You should have received a copy of the GNU Lesser General
#  Public License along with HCSS.
#  If not, see <http://www.gnu.org/licenses/>.
# 
###########################################################################
###            SPIRE Small Map Mode User Reprocessing Script          ###
###########################################################################
#  Purpose:  A simplified version of SPIRE Small Map Mode POF10 pipeline   
#            script distributed with HIPE 10.0.  This is for data reprocessing
#             by a user using the latest SPIRE calibration products.
# 
#            The results are three FITS files with extensions for the PSW,  
#            PMW, PLW arrays containing the final,
#            - image map  
#            - error map  
#            - coverage map  
#    
#  Usage:    The user needs to specify the options in the simple user input 
#            section at the beginning of the script;
#            - Observation ID (obsid)  
#            - Data pool name  
#            - Output directory for final fits files
#
# Note:  it is possible to save entire observation back to a pool by
#     uncommenting the saveObservation command at the end of the script
#
#  Assumptions: A data pool has already been created on disk. 
#               The data has already been processed to Level 0.5
#
#  Updated: 21/12/2012
#
###########################################################################



###########################################################################
###                     User Selectable Options                         ###
###########################################################################
# (A) Specific OBSID in the form of an integer or hexadecimal (0x) number: 
# (B) the name of the data Pool in your Local Store:
# (C) Specify the output directory for writing the maps FITS files:
#
myObsid    =  1342220542
myDataPool = "1342220542"
outDir     = "C:\\Users\\yfjin\\hcss\\workresult\\"
# e.g.
#myObsid    =  0x5000489F
#myDataPool = "OD358-SmallScanMapGammDra0x5000489F"
#outDir     = "/Users/cpearson/jython/localstore/plots/"
#
# Additional Options
# (D) mapping: The mapping Algorithm to use naive or madmap
# (E) includeTurnaround: Include the scan line turnarounds in the pocessing and mapmaking
# (F) applyExtendedEmissionGain: Apply the relative gains for each bolometer for extended emission
# (G) baselineSubtraction: Subtract a baseline from each scan to avoid stripes
# (H) destriper: Determine and remove baselines to achive an optimum fit between all timelines
#     If the map maker is 'naive', at least one of the options G or H must be True.


mapping = 'naive'
includeTurnaround = False
applyExtendedEmissionGains = False
useBaselineSubtraction = False
useDestriper = True
###########################################################################



#*************************************************************************
##  Load in an observation context from your data pool into HIPE:
obs=getObservation(myObsid,poolName=myDataPool)

print
print "Processing observation %i (0x%X) from data pool %s."%(myObsid, myObsid, myDataPool)

#*************************************************************************
# Calibration Context and Calibration Files 
# Read the latest calibration tree relevant to HCSS v10 from the local disc:

cal = spireCal(pool="spire_cal_10_1")

# TO CORRECT AN ERROR ON THE ABOVE LINE, run the following command ONCE only
# to load and save the calibration tree from the Archive (may take some time):
# (for more details, see the "Calibration" chapter in the SPIRE Data Reduction Guide)

#cal = spireCal(calTree="spire_cal_10_1", saveTree=True)

# Attach the updated calibration tree to the observation context
obs.calibration.update(cal)



# Extract necessary Calibration Products from the Observation Context
bsmPos             = obs.calibration.phot.bsmPos
lpfPar             = obs.calibration.phot.lpfPar
detAngOff          = obs.calibration.phot.detAngOff
elecCross          = obs.calibration.phot.elecCross
chanTimeConst      = obs.calibration.phot.chanTimeConst
chanNum            = obs.calibration.phot.chanNum
fluxConvList       = obs.calibration.phot.fluxConvList
tempDriftCorrList  = obs.calibration.phot.tempDriftCorrList
chanRelGains       = obs.calibration.phot.chanRelGain
chanNoiseList      = obs.calibration.phot.chanNoiseList
chanNoise          = chanNoiseList.getProduct(obs.level1.getProduct(0).meta["biasMode"].value,obs.level1.getProduct(0).startDate)

# Note to read in a single calibration fits file from some location use, e.g., 
# bsmPos = simpleFitsReader("/enter/path/here/"+"YourCalibrationFilename.fits")

# Extract the necessary Auxiliary Products from the Observation Context
hpp      = obs.auxiliary.pointing
siam     = obs.auxiliary.siam
timeCorr = obs.auxiliary.timeCorrelation
#*************************************************************************


#*************************************************************************
## Reports how many scan lines there are to process
count=1
bbids=obs.level0_5.getBbids(0xa103)
nlines=len(bbids)
print "Total number of scan lines: ",nlines
print
# Create Level1 context to collect Level one products
level1=Level1Context(myObsid)

#
###########################################################################
###   Pipeline Level 0.5 to Level 1                                     ###
###   Process all Building Blocks for this observation                  ###
###########################################################################
# Loop over scan lines
for bbid in bbids:
    print "Starting BBID=0x%x: scan %i / %i"%(bbid,count,nlines)
    # Get basic level 0.5 data products (detector data and housekeeping data) 
    pdt  = obs.level0_5.get(bbid).pdt
    nhkt = obs.level0_5.get(bbid).nhkt
    # record the calibration tree version used by the pipeline
    pdt.calVersion = obs.calibration.version
    #
    # -----------------------------------------------------------
    # (1) join all scan legs and turnarounds together
    bbCount=bbid & 0xFFFF
    pdtLead=None
    nhktLead=None
    pdtTrail=None
    nhktTrail=None
    if bbCount >1:
        blockLead=obs.level0_5.get(0xaf000000L+bbCount-1)
        pdtLead=blockLead.pdt
        nhktLead=blockLead.nhkt
        if pdtLead != None and pdtLead.sampleTime[-1] < pdt.sampleTime[0]-3.0:
            pdtLead=None
            nhktLead=None
    if bbid < MAX(Long1d(bbids)):
        blockTrail=obs.level0_5.get(0xaf000000L+bbCount)
        pdtTrail=blockTrail.pdt
        nhktTrail=blockTrail.nhkt
        if pdtTrail != None and pdtTrail.sampleTime[0] > pdt.sampleTime[-1]+3.0:
            pdtTrail=None
            nhktTrail=None
    pdt=joinPhotDetTimelines(pdt,pdtLead,pdtTrail)
    nhkt=joinNhkTimelines(nhkt,nhktLead,nhktTrail)
    #
    # -----------------------------------------------------------
    # (2) Convert BSM timeline to angles on sky (constant for scan map)
    bat=calcBsmAngles(nhkt,bsmPos=bsmPos)
    #
    # -----------------------------------------------------------
    # (3) Create the Spire Pointing Product for this observation
    spp=createSpirePointing(detAngOff=detAngOff,bat=bat,hpp=hpp,siam=siam)
    #
    # -----------------------------------------------------------
    # (4) Run the Electrical Crosstalk Correction on the timeline data
    pdt=elecCrossCorrection(pdt,elecCross=elecCross)
    #
    # -----------------------------------------------------------
    # (5) Detect jumps in the Thermistor timelines that occasionally occur,
    # leading to map artefacts introduced in the temperature drift correction
    # Also requires the Temperature Drift Correct Calibration File.
    tempDriftCorr=tempDriftCorrList.getProduct(pdt.meta["biasMode"].value,pdt.startDate)
    if pdt.meta["biasMode"].value == "nominal":
        pdt=signalJumpDetector(pdt,tempDriftCorr=tempDriftCorr, kappa=2.0,gamma=6.0,\
            gapWidth=1.0,windowWidth=40.0, filterType="DISCRETEDERIVATIVE",glitchinfo="NULL")
    #
    # -----------------------------------------------------------
    # (6) Run the concurrent deglitcher on the timeline data
    pdt=concurrentGlitchDeglitcher(pdt,chanNum=chanNum,kappa=2.0, size = 15, correctGlitches = True)
    #
    # -----------------------------------------------------------
    # (7) Run the wavelet deglitcher on the timeline data
    pdt=waveletDeglitcher(pdt, scaleMin=1.0, scaleMax=8.0, scaleInterval=7, holderMin=-3.0,\
			holderMax=-0.3, correlationThreshold=0.3, optionReconstruction='linearAdaptive20',\
			reconstructionPointsBefore=1, reconstructionPointsAfter=3)
    #
    # Alternatively, run the sigma-kappa deglitcher.
    # The following task can be uncommented to try the sigma-kappa deglitcher.
    # In this case the wavelet deglitcher should be commented out.
    # This module is still a prototype and should be used with caution.
    #pdt = sigmaKappaDeglitcher(pdt,
    #            filterType="BOXCAR", boxFilterWidth = 3, \
    #            boxFilterCascade = 1, kappa = 4.0, \
    #            disableSigmaKappaDetection = 'NULL', \
    #            largeGlitchMode = 'ADDITIVE', \
    #            largeGlitchDiscriminatorTimeConstant = 4, \
    #            largeGlitchRemovalTimeConstant = 6, \
    #            disableLargeGlitchDetection = 'NULL', \
    #            correctionMode = 'DIRECT', gamma = 1.0, \
    #            randomSeed = 1984574303L, \
    #            disableGlitchReconstruction = 'NULL', \
    #            iterationNumber = 1)
    #
    # -----------------------------------------------------------
    # (8) Apply the Low Pass Filter response correction
    pdt=lpfResponseCorrection(pdt,lpfPar=lpfPar)
    #
    # -----------------------------------------------------------
    # (9) Apply the flux conversion 
    fluxConv=fluxConvList.getProduct(pdt.meta["biasMode"].value,pdt.startDate)
    pdt=photFluxConversion(pdt,fluxConv=fluxConv)
    #
    # -----------------------------------------------------------
    # (10) Make the temperature drift correction
    pdt=temperatureDriftCorrection(pdt,tempDriftCorr=tempDriftCorr)
    #
    # -----------------------------------------------------------
    # (11) Apply the bolometer time response correction
    pdt=bolometerResponseCorrection(pdt,chanTimeConst=chanTimeConst)
    #
    # -----------------------------------------------------------
    # (12) Cut the timeline back into individual scan lines .
    pdt=cutPhotDetTimelines(pdt,extend=includeTurnaround)
    #
    # -----------------------------------------------------------
    # (13) Add pointing timelines to the data
    psp=associateSkyPosition(pdt,spp=spp)
    #
    # -----------------------------------------------------------
    # (14) Apply the time correlation 
    psp=timeCorrelation(psp,timeCorr)
    #
    # -----------------------------------------------------------
    # Add Photometer Scan Product to Level 1 context
    level1.addProduct(psp)
    #
    print "Completed BBID=0x%x (scan %i/%i)"%(bbid,count,nlines)
    # set the progress
    count=count+1
print
print "Finished the Level 0.5 to Level 1 processing for OBSID= %i, (0x%x)"%(myObsid,myObsid)
# Update the Level 1 Context in the Observation Context
obs.level1 = level1
#
###            Finished the Level 0.5 to Level 1 processing             ###
###########################################################################



###########################################################################
###   Optionally apply Relative Bolometer Gains for extended emission   ###
###########################################################################
if applyExtendedEmissionGains:
    print
    print "Apply relative gains for bolometers for better extended maps"
    for i in range(level1.getCount()):
        level1.getRefs().set(i,ProductRef(applyRelativeGains(level1.getProduct(i), gains = chanRelGains)))
    print "Finished applying relative gains"
    print
###             Finished applying relative gains                        ###
###########################################################################



###########################################################################
###                      Baseline Subtraction                           ###
###########################################################################
if useBaselineSubtraction:
    print
    print "Begin the Baseline Subtraction for OBSID= %i, (0x%x)"%(myObsid,myObsid)
    #
    # Using Level 1 context. Run baseline removal  as an input to the map making
    scans=baselineRemovalMedian(level1)
    print "Finished the Baseline Subtraction for OBSID= %i, (0x%x)"%(myObsid,myObsid)
    print
else:
    scans = obs.level1
###                   Finished the Baseline Subtraction                 ###
###########################################################################



###########################################################################
###                      Destriping                                     ###
###########################################################################
if useDestriper:
    print
    print "Destriper Run for OBSID= %i, (0x%x)"%(myObsid,myObsid)
    arrays = ["PSW","PMW","PLW"]
    pixelSize = [6,10,14]  #Map pixel size in arcsec for PSW, PMW, PLW respectively
    maps = []
    #
    # Using Level 1 context. Run destriper as an input to the map making
    for iArray in range(len(arrays)):
        scans,map,diag,p4,p5 = destriper(level1=scans,\
            pixelSize=pixelSize[iArray], offsetFunction='perScan',\
            array=arrays[iArray], polyDegree=0, kappa=5.0, iterThresh=1.0E-10,\
            l2DeglitchRepeat=100, l2DeglitchAlgorithm='sigmaKappa',\
            iterMax=100, l2IterMax=5, nThreads=2, withMedianCorrected=True,\
            brightSource=True, useSink=False, storeTod=False)
        #
        # Save diagnostic product
        if obs.level2.refs['pdd'+arrays[iArray]]!=None: obs.level2.refs.remove('pdd'+arrays[iArray])
        obs.level2.setProduct('psrc'+arrays[iArray]+'diag', diag)
        #
        # Keep destriper maps for inspection
        maps.append(map)
    pass
    print "Finished the Destriper Run for OBSID= %i, (0x%x)"%(myObsid,myObsid)
    print
###                   Finished Destriping                               ###
###########################################################################


###########################################################################
### Update Level 1 with the destriped/baseline subtracted timeline data ###
###########################################################################
obs.level1=scans
#
###                   Finished Update                                   ###
###########################################################################


###########################################################################
###                          Mapmaking                                  ###
###########################################################################
# 
# Either the Naive Map maker
# For alternative weighted error map use (requires Channel Noise Table Calibration Product);
# naiveScanMapper(scans,array="PSW",method=WhiteNoiseWeight,chanNoise=chanNoise)
if mapping == 'naive':
    print 'Starting Naive Map maker'
    mapPlw=naiveScanMapper(scans, array="PLW", method=BinaryWeightStrategy)
    mapPmw=naiveScanMapper(scans, array="PMW", method=BinaryWeightStrategy)
    mapPsw=naiveScanMapper(scans, array="PSW", method=BinaryWeightStrategy)
else:
# -----------------------------------------------------------
# or the Mad Map Map maker (requires Channel Noise Table Calibration Product)
    print 'Starting Mad Mapper'
    mapPlw=madScanMapper(scans, array="PLW",chanNoise=chanNoise)
    mapPmw=madScanMapper(scans, array="PMW",chanNoise=chanNoise)
    mapPsw=madScanMapper(scans, array="PSW",chanNoise=chanNoise)
pass
# Update the Level 2 (point source maps) Context in the Observation Context
# Clean contxt of pre-HIPE 10 products
if obs.level2.refs['PSW']!=None: obs.level2.refs.remove('PSW')
if obs.level2.refs['PMW']!=None: obs.level2.refs.remove('PMW')
if obs.level2.refs['PLW']!=None: obs.level2.refs.remove('PLW')
obs.level2.setProduct("psrcPSW", mapPsw)
obs.level2.setProduct("psrcPMW", mapPmw)
obs.level2.setProduct("psrcPLW", mapPlw)
#
print "Finished the map making for OBSID= %i, (0x%x)"%(myObsid,myObsid)

print
#
#
# -----------------------------------------------------------
# Save Maps to output directory
simpleFitsWriter(mapPsw, "%smapPSW_%i.fits"%(outDir, myObsid))
simpleFitsWriter(mapPmw, "%smapPMW_%i.fits"%(outDir, myObsid))
simpleFitsWriter(mapPlw, "%smapPLW_%i.fits"%(outDir, myObsid))
print "Map saved as FITS files to %s"%(outDir)
#
###                Finished the Mapmaking                                ###
############################################################################

# Finally we can save the new reprocessed observation back to your hard disk
# Uncomment the next line and choose a poolName, either the existing one or a new one
#
#saveObservation(obs,poolName="enter-a-poolname",saveCalTree=True)

#
print
print "Completed the processing of OBSID= %i, (0x%x)"%(myObsid,myObsid)



#### End of the script ####

endPipeline=time.clock()
TPipeline=endPipeline-beginPipeline
print TPipeline
Double1dNumCount.Double1dGetALL()
Double2dNumCount.Double2dGetALL()
Complex1dNumCount.Complex1dGetALL()
MatrixNumCount.MatrixGetALL()
FFTNumCount.FFTGetALL()
SVDNumCount.SVDGetALL()