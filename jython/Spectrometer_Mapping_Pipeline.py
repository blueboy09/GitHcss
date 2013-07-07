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
###          SPIRE Spectrometer Mapping User Reprocessing Script        ###
###########################################################################
#  Purpose:  A simplified version of the SPIRE mapping pipeline script. 
#            This script allows to reprocess (A) a specific observation 
#            using the latest SPIRE calibration products. The user 
#            can (C) produce either unapodized or apodized 
#            spectra. (D) An output directory is required to store 
#            results as FITS files containing the final spectral 
#            cubes and one spectrum file per jiggle position. (E) For 
#            observations taken in High + Low Resolution mode, the user 
#            must select whether to process data in high or low resolution.
#            (F) The user must specify the size of the spatial pixels of 
#            the resulting cubes.
#
#  Usage:    The user needs to specify the options in the section
#            "User Selectable Options" at the beginning of the script.
#
#  Updated:  21/Dec/2012
#
###########################################################################

###########################################################################
###                     User Selectable Options                         ###
###########################################################################
#
# (A) Specify OBSID:
myObsid = 1342208388
#
# (B) N/A
#
# (C) The final spectrum will be unapodized (apodize = 0) or 
#     apodized (apodize = 1):
apodize = 0
if apodize:
    apodName="aNB_15"
else:
    apodName="unapod"
#
# (D) Specify the output directory for writing the resulting spectra and 
#     cubes into FITS files:
outDir = "C:\\Users\\yfjin\\hcss\\workresult\\"
#
# (E) For H+L observations only - changing this option has no effect for
#     observations that were not observed in "High+Low" mode:
#     Choose whether to process LR or HR data (from a HR+LR observation)
processRes="LR"
#
# (F) Specify the map pixel size for the final data cubes (SSW and SLW)
#     depending on the spatial sampling in units of degree:
sswFwhm = 19.0 / 3600.0
slwFwhm = 35.0 / 3600.0
gridSpacing={"full":        {"SSW": 0.5 * sswFwhm, "SLW": 0.5 * slwFwhm}, \
             "intermediate":{"SSW": 1.0 * sswFwhm, "SLW": 1.0 * slwFwhm}, \
             "sparse":      {"SSW": 2.0 * sswFwhm, "SLW": 2.0 * slwFwhm}}
#
###########################################################################

# Define the thermistors, dark pixels and resistors:
thermistors = ["SLWR1","SSWR1","SLWT1","SLWT2","SSWT1","SSWT2",\
               "SSWDP1","SSWDP2","SLWDP1","SLWDP2"]

# Load an observation context into HIPE:
obs = getObservation(myObsid)
# To specify a pool name use:
# obs = getObservation(myObsid, poolName="poolName") 
# To load data directly from the HSA use:
# obs = getObservation(myObsid, useHsa=True)

print "Processing observation %i (0x%X)"%(myObsid, myObsid)
         
# Calibration Context and Calibration Files 
# Read the latest calibration tree relevant to HCSS v10 from the local disc:
cal = spireCal(pool="spire_cal_10_1")
# TO CORRECT AN ERROR ON THE ABOVE LINE, run the following command once only
# to load and save the calibration tree from the Archive (may take some time):
# (for more details, see the "Calibration" chapter in the SPIRE
# Data Reduction Guide)

#cal = spireCal(calTree="spire_cal_10_1", saveTree=True)

# Attach the updated calibration tree to the observation context
obs.calibration.update(cal)

# Find out the bias mode of the observation (nominal/bright)
biasMode = obs.meta["biasMode"].value

# Extract necessary Calibration Products from the Observation Context
nonLinCorr     = obs.calibration.spec.nonLinCorr
tempDriftCorr  = obs.calibration.spec.tempDriftCorr
chanNum        = obs.calibration.spec.chanNum
bolPar         = obs.calibration.spec.bolPar
nomPcal        = obs.calibration.spec.nomPcal
pcalModel      = obs.calibration.spec.pcalModel
lpfPar         = obs.calibration.spec.lpfPar
phaseCorrLim   = obs.calibration.spec.phaseCorrLim
chanTimeConst  = obs.calibration.spec.chanTimeConst
bsmPos         = obs.calibration.spec.bsmPos
detAngOff      = obs.calibration.spec.detAngOff
smecZpd        = obs.calibration.spec.smecZpd
chanTimeOff    = obs.calibration.spec.chanTimeOff
smecStepFactor = obs.calibration.spec.smecStepFactor
opdLimits      = obs.calibration.spec.opdLimits
bandEdge       = obs.calibration.spec.bandEdge
brightGain     = obs.calibration.spec.brightGain
teleModel      = obs.calibration.spec.teleModel

# Extract necessary Auxiliary Products from the Observation Context
hpp  = obs.auxiliary.pointing
siam = obs.auxiliary.siam
hk   = obs.auxiliary.hk

# Reprocess the observation from Level-0 to Level-0.5 for Bright mode only
# (for nominal mode, use the Level-0.5 data directly from the observation)
if biasMode == "nominal":
    level0_5 = obs.level0_5
elif biasMode == "bright":
    level0_5 = engConversion(level0=obs.level0, cal=obs.calibration, usePhases=True)
    # Save the processed Level-0.5 data back into the Observation Context:
    obs.level0_5 = level0_5

# For Bright mode only: process the PCAL flash building block (0xb6b9)
if biasMode == "bright":
    sdt  = level0_5.get(0xb6b90001).sdt
    scut = level0_5.get(0xb6b90001).scut
    sdt  = calcOpticalPower(sdt, chanNum=chanNum, bolPar=bolPar, computeRes=True, \
                            signalTable="temperature")
    # Consult the Pipeline Specification Manual for more options of the sigmaKappaDeglitcher
    sdt = sigmaKappaDeglitcher(sdt, kappa=4.0, largeGlitchMode="ADDITIVE", \
                               largeGlitchDiscriminatorTimeConstant=4,\
                               largeGlitchRemovalTimeConstant=6)
    specPcal = pcal(sdt, scut=scut, pm=pcalModel)

# Start to process the observation from Level 0.5
# Process each SMEC scan building block (0xa106) individually, append to a list 
sdsList = SpireMapContext()
# Each building block is a different jiggle position
for bbid in level0_5.getBbids(0xa106):
    print"Processing building block 0x%X (%i/%i)"%(bbid, bbid-0xa1060000L, len(obs.level0_5.getBbids(0xa106)))
    sdt   = level0_5.get(bbid).sdt
    # Record the calibration tree version used by the pipeline:
    sdt.calVersion = obs.calibration.version
    nhkt  = level0_5.get(bbid).nhkt
    smect = level0_5.get(bbid).smect
    bsmt  = level0_5.get(bbid).bsmt
    # Extract the jiggle ID from the metadata:
    jiggId = sdt.meta["jiggId"].value
    # Extract raster ID from the metadata:
    raster = sdt.meta["pointNum"].value
    # -----------------------------------------------------------
    # 1st level deglitching:    
    # Consult the Pipeline Specification Manual for more options of the waveletDeglitcher
    sdt = waveletDeglitcher(sdt, optionReconstruction="polynomialAdaptive10")
    # -----------------------------------------------------------
    if biasMode == "nominal":
        # Run the Non-linearity and Temperature Drift correction steps:
        sdt = specNonLinearityCorrection(sdt, nonLinCorr=nonLinCorr)
        sdt = temperatureDriftCorrection(sdt, tempDriftCorr=tempDriftCorr)
        # Remove the thermistors, dark pixels and resistors:
        sdt = filterChannels(sdt, removeChannels=thermistors, keepSet="UNVIGNETTED")
    elif biasMode == "bright":
        # Convert the voltage to bolometer temperature (bright source setting only):
        sdt = calcOpticalPower(sdt, chanNum=chanNum, bolPar=bolPar, computeRes=True, \
                               signalTable="temperature")
        # Remove the thermistors, dark pixels and resistors:
        sdt = filterChannels(sdt, removeChannels=thermistors, keepSet="UNVIGNETTED")
        # Apply bright PCAL gain (bright source setting only):
        sdt = specApplyPcalGain(sdt, nomPcal=nomPcal, specPcal=specPcal)
    # -----------------------------------------------------------
    # Repair clipped samples where needed:
    sdt = clippingCorrection(sdt)
    # -----------------------------------------------------------
    # Time domain phase correction:
    sdt = timeDomainPhaseCorrection(sdt, nhkt, lpfPar=lpfPar, \
               phaseCorrLim=phaseCorrLim, chanTimeConst=chanTimeConst)        
    # -----------------------------------------------------------
    # Add pointing info:
    bat = calcBsmAngles(bsmt, bsmPos=bsmPos)
    spp = createSpirePointing(hpp=hpp, siam=siam, \
                            detAngOff=detAngOff, bat=bat)
    # -----------------------------------------------------------
    # Create interferogram:
    sdi = createIfgm(sdt, smect=smect, nhkt=nhkt, spp=spp, \
                     smecZpd=smecZpd,\
                     chanTimeOff=chanTimeOff,\
                     smecStepFactor=smecStepFactor)
    # -----------------------------------------------------------
    # Update the resolution if processing a H+L observation as LR
    if obs.meta["commandedResolution"].value == "H+LR" and processRes == "LR":
        sdi.processResolution = "LR"
    # Adjust OPD ranges to ensure that they are the same for all scans
    sdi = makeSameOpds(sdi, opdLimits=opdLimits)
    # -----------------------------------------------------------
    # Baseline correction:
    sdi = baselineCorrection(sdi, type="fourier", threshold=4) 
    # -----------------------------------------------------------
    # 2nd level deglitching:
    sdi = deglitchIfgm(sdi, deglitchType="MAD")
    # -----------------------------------------------------------
    # Phase correction
    # The phase correction is calculated from an averaged LR interferogram:
    avgSdiFull = averageInterferogram(sdi)
    lowResSdi  = avgSdiFull.copy()
    lowResSdi.processResolution = "LR"
    lowResSdi  = makeSameOpds(lowResSdi, opdLimits=opdLimits)
    # Apply the phase correction:
    sdi = phaseCorrection(sdi, avgSdi=lowResSdi, avgSdiFull=avgSdiFull, spectralUnit="GHz")
    # -----------------------------------------------------------
    # Fourier transform:
    ssds = fourierTransform(sdi, ftType="postPhaseCorr", zeroPad="standard", \
                            spectralUnit="GHz")
    # -----------------------------------------------------------
    # Get the RSRF calibration products
    # Note: this will only work if the raw data was processed with HIPE v7 and above
    # If you get an error here, redownloading the observation from the HSA should fix it
    instRsrf = obs.calibration.spec.instRsrfList.getProduct(ssds)
    teleRsrf = obs.calibration.spec.teleRsrfList.getProduct(ssds)
    # -----------------------------------------------------------
    # Remove out of band data:
    ssds = removeOutOfBand(ssds, bandEdge=bandEdge)
    # -----------------------------------------------------------
    # Apply bright gain correction (bright source setting only):
    if biasMode == "bright":
        ssds = specApplyBrightGain(ssds, brightGain=brightGain)
    # -----------------------------------------------------------
    # Correction for instrument emission:
    ssds = instCorrection(ssds, nhkt=nhkt, instRsrf=instRsrf)
    # -----------------------------------------------------------
    # Get the flux conversion calibration products and apply to spectra:
    ssds = specExtendedFluxConversion(ssds, teleRsrf=teleRsrf)
    # -----------------------------------------------------------
    # Correction for telescope emission:
    ssds = telescopeCorrection(ssds, hk=hk, teleModel=teleModel)
    # ----------------------------------------------------------- 
    # Apodization (if required):
    if apodize:
        sdi = inverseFourierTransform(ssds)
        sdi = apodizeIfgm(sdi, apodType="postPhaseCorr", apodName=apodName)
        ssds = fourierTransform(sdi, ftType="postPhaseCorr", zeroPad="standard",\
                                spectralUnit="GHz")
        ssds = removeOutOfBand(ssds, bandEdge=bandEdge)
    # ----------------------------------------------------------- 
    # Append this scan to the list, taking account whether the resolution
    # was H+L or not
    if obs.meta["commandedResolution"].value == "H+LR":
        # for processing all scans as LR
        if processRes == "LR":
            sdsList.setProduct("%d"%(sdsList.refs.size()), ssds)
            # Save individual FITS files
            simpleFitsWriter(ssds, "%s%i_spectrum_%s_%s_%i_%i.fits"%(outDir, \
                myObsid, ssds.processResolution, apodName, raster, bbid-0xa1060001L))
        # for processing the HR scans
        elif processRes == ssds.processResolution:
            sdsList.setProduct("%d"%(sdsList.refs.size()), ssds)
            # Save individual FITS files
            simpleFitsWriter(ssds, "%s%i_spectrum_%s_%s_%i_%i.fits"%(outDir, \
                myObsid, ssds.processResolution, apodName, raster, bbid-0xa1060001L))
    # or, otherwise
    else:
        sdsList.setProduct("%d"%(sdsList.refs.size()),ssds)
        # Save individual FITS files:
        simpleFitsWriter(ssds, "%s%i_spectrum_%s_%s_%i_%i.fits"%(outDir, \
            myObsid, ssds.processResolution, apodName, raster, bbid-0xa1060001L))
    # -----------------------------------------------------------
    # Save the Level-1 data back into the Observation Context:
    if obs.level1:
        res = ssds.processResolution
        # Check the resolution for backwards compatibility with old Obs Contexts:
        if not obs.level1.refs.containsKey("Point_0_Jiggle_0_%s"%res):
            res = ssds.commandedResolution
        # Save the products back into the right places inside the Observation Context
        obs.level1.getProduct("Point_%i_Jiggle_%i_%s"%(raster,\
            jiggId, res)).setProduct("interferogram", sdi)
        if apodize:
            obs.level1.getProduct("Point_%i_Jiggle_%i_%s"%(raster,\
             jiggId, res)).setProduct("apodized_spectrum", ssds)
        else:
            obs.level1.getProduct("Point_%i_Jiggle_%i_%s"%(raster,\
             jiggId, res)).setProduct("unapodized_spectrum", ssds)

# ---------------------------------------------------------------
# Carry out regridding
mapSampling = obs.meta['mapSampling'].value
for array in ["SSW", "SLW"]:
    # Create a pre-processed cube (not regularly gridded):
    preCube = spirePreprocessCube(context=sdsList, arrayType=array, unvignetted=True)
    # Set up the grid - covering the RA and Dec of observed points using specified gridSpacing:
    wcs = SpireWcsCreator.createWcs(preCube, gridSpacing[mapSampling][array], gridSpacing[mapSampling][array])
    # Regrid the data using the Naive Projection algorithm:
    if array == "SSW": 
        cube = cubeSSW = spireProjection(spc=preCube, wcs=wcs, projectionType="naive")
    elif array == "SLW": 
        cube = cubeSLW = spireProjection(spc=preCube, wcs=wcs, projectionType="naive")
    # Save the cube to FITS:
    simpleFitsWriter(cube, "%s%i_%s_%s_%s_cube.fits"%(outDir, myObsid, \
                     cube.meta["processResolution"].value, array, apodName))
    # Save the processed products back into the Observation Context:
    if obs.level2 and not apodize:
        obs.level2.setProduct("%s_%s_unapodized_spectrum"%(res, array), cube)
    elif obs.level2 and apodize:
        obs.level2.setProduct("%s_%s_apodized_spectrum"%(res, array), cube)

# Finally we can save the new reprocessed observation back to your hard disk.
# Note that only the parts of the Observation Context covered by the script
# will have been updated! (i.e. apodized/unapodized products).
# Uncomment the next line and choose a poolName, either the existing one or a new one
#saveObservation(obs, poolName="enter-a-poolname", saveCalTree=True)

print "Processing of observation %i (0x%X) complete"%(myObsid, myObsid)
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