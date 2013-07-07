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
#  Copyright 2001-2011 Herschel Science Ground Segment Consortium
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


"""
TIP: if you edit this script in hipe:
- all lines of code actually executed by this script will appear in black
- all comments and explanations will appear in green
- all line of codes that are not executed by default but that could be useful
in some particular cases, will appear in red

if you want to edit the script and remove comments and commented lines of code,
be careful in preserving the indentation. Otherwise if statements and loop
might not work. 

 This script processes scan map and mini scan map observations from Level 0
 (raw data) up to Level 2 (final map). There are two flavors for the map
 projection: the highpass filter way and the MadMap algorithm. This script
 is using the highpass filter way to remove the 1/f noise. This method is
 recommended for point sources (the usual case  for mini scan map and deep
 fields) and relatively small extended sources since it removes large scale
 structures that can not be properly masked (see below for details) in the
 processing.

 This script can be used to reduce a single obsid or can be called in a loop
 (see the multiple_obsid_scanmap_Deep_survey_miniscan_Pointsource.py) to reduce
 many obsid. The script is divided in sections. The user can just comment or
 uncomment several sections to start the data reduction from different product
 Levels or to use the script in a loop. The script contains the following
 sections:

 - SECTION 0 : this section contains the obsid number, camera, hpfradius and
               other settings. This section can be completely commented out if
               the user wants to use this script in a loop. In this case
               the settings will be contained in the 
               multiple_obsid_scanmap_Deep_survey_miniscan_Pointsource.py 
               script, which performs the loop over a list of obsid numbers.

 - SECTION 1 : this section let the user access the observation and the 
               auxiliary data from HSA or from a preexisting pool. In this
               section the data are reduced up the level 0.5. After this level
               the auxiliary data are not needed for the further data reduction
               and the Level 0.5 product is saved in fits file.

 - SECTION 2 : This section starts from the Level 0.5 product and reduce the
               data up to Level 1. The user can choose to start the data
               reduction from this section if the Level 0.5 product is saved
               in fits file. This can be easily done by commenting the whole
               section 1 and by uncommenting two lines of code where the fits
               file of the Level 0.5 data is read.  At the end of this section
               Level 1 data are saved in fits file as well.

 - SECTION 3 : This section start from the Level 1 product and reduce the data
               up to Level 2. The user can choose to start the data reduction
               from this section if the Level 1 data are saved in fits file.
               This can be easily done by commenting the whole sections 1 and
               2 and by uncommenting two lines of code where the fits file of
               the Level 1 data is read.  At the end of this section the final
               map is saved in fits file as well. This section includes several
               options to reduce the data with different masking methods.



############################ SECTION 0 #########################################
################################################################################
############################ SETTINGS ##########################################

 The input_setting variable is used here to check whether the settings are
 already given in the multiple_obsid script in order to avoid overwriting. 
 If input_setting  is set to True the script will keep the settings given in
 the corresponding multiple obsid script. If input_setting  is set to False,
 the script will read the settings in this section.
"""
try:
  input_setting
  print "settings given in the multiple obsid script"
except:
  input_setting=False


if input_setting==False:
  print "input parameters set in the individual obsid script"
# 
# directory name where to read or save files. 
#  direc = "/your_favorite_output_directory/"
#  direc = "C:\\Users\\yfjin\\.hcss\\lstore\\1342220914\\"
  direc = "C:\\Users\\yfjin\\hcss\\fitresult\\"
 
  """
 The settings for this data reduction are collected all in this section. 
 If the user wants to use this script in the loop contained in the
 multiple_obsid_Brightsource.py, this section can be completely commented out
 and the settings will be contained in the multiple_obsid.py script .
  """
#
#  obsid="000000000"  #give here the obsid number
  obsid="1342220914"
#  obsid="1342186275"
#  camera = "red"
  camera="blue"
  print "Reducing OBSID:", obsid, "camera:", camera
  """
 settings output map pixel size: the choice of the output pixel size depends
 on the redundancy of your  observation and on the drop size you chose for
 the drizzling method implemented in the projection task,  PhotProject.
 See the PACS Data Reduction Guide or the PACS User Manual for more details
 about the choice of those parameters. Here we set the output pixel size
 to 2 arcsec for the blue channel and 3 arcsec for the red channel. These
 parameter values are found to work generally well with a drop size (pixfrac)
 1/10 of input pixel size. Anyhow, we invite the user to play with these values
 to find the optimal combination for the specific scientific case.
 See below for more details about the meaning of these parameters.
 """
  if camera=='blue':
     outpixsz=2.
  elif camera=='red':
     outpixsz=3.
#
  pixfrac=0.1 
  """
 setting of the highpass filter radius in number of readouts. The following
 numbers are suited for point sources. Larger radii should be set for very
 bright or extended sources with the caveat that the 1/f noise will not be
 properly removed. As a general rule, the smaller the high pass filter radius,
 the better you remove the 1/f noise. The suggested values allow to remove as
 much as possible the 1/f without damaging the PSF. Alternative values  have
 to be chosen on the basis of the source dimension. As a rule of thumb the
 hpfradius should be as large as  the source (mask) size. However, if the
 interpolation method is used in the high-pass filter task, hpfradius can be
 smaller then the source size. In general, values larger that 100 readouts
 are not recommended.
  """
  if camera=='blue':
     hpfradius=15
  elif camera=='red':
     hpfradius=25
  """
 option chosen for the source masking (see details at the beginning of
 SECTION 3)
  """
#
  option = 1
#
  """
 If you have already a mask of the sources, you can provide here the file
 name and choose the option=2
  """
#
# maskfile=direc+ "mask_file_name"
# option = 2
#
elif input_setting==True:
  print "settings given in multi_obsid script"

"""
########################### END OF SECTION 0 ###################################

################################ SECTION 1 #####################################
################################################################################
################ IF YOU ARE ACCESSING THE DATA FOR THE FIRST TIME ##############
############### START FROM HERE OTHERWISE GO TO THE NEXT SECTION ###############
################################################################################
 here the script accesses the data: we list three different options to do that 

############# FIRST OPTION: getting the data from the tar-file #################


 We suppose you already got your tar file containing your data
 (Observation Context) from HSA. Here we show how to access the data from
 the Observation Context you got in the tar-file
  !!!!!!!!!!!!!! TO BE INCLUDED !!!!!!!!!!!!!!!!



################# SECOND OPTION: via HSA login #################################

 edit login information here (OR IN THE FILE .hcss/user.props)  ###############
bn

 If you did not get your Observation Context, then there are another way you
 can access the data, directly from the HSA. Here we show how to do that.

 A TIP: hipe choses by default as local store the directory .hcss/lstore/ in
 your home. If you prefer to store the data somewhere else, e.g. a disk with
 more space, then type this extra line before accessing the archive to let
 hipe know where to store the data. 
"""
#Configuration.setProperty("hcss.ia.pal.pool.lstore.dir", "/favorite_local_store_directory/")
"""
 the next few lines of code set your username and password to accsess your
 data through the HSA. If you have already set these variables into your
 user_prop file according to the User Manual, you can delete or leave
 commented the following four lines
"""
#login_usr = "hcss.ia.pal.pool.hsa.haio.login_usr"
#login_pwd = "hcss.ia.pal.pool.hsa.haio.login_pwd"
#Configuration.setProperty(login_usr,"username")
#Configuration.setProperty(login_pwd,"password")
"""
 A TIP: sometimes it can happen that previously stored data in the local
 pool conflict with a new download. For instance it might happen that an
 observation reduced without problem the first time can not be reduced anymore
 because part of the data, e.g. the auxiliary data, can not be retrieved
 anymore. If this happens, it might be useful to remove or simply move
 somewhere else the .hcss/pal_cashe/ and the
 /favorite_local_store_directory/has_cashe/ and repeat the data reduction.
"""
#obs = getObservation(obsid, useHsa=True, instrument='PACS')
#
"""
############## THIRD OPTION: retrieve the observation context ##################
############### from a local pool after EDITING the ############################
################## poolLocation directory ######################################
"""
dir = 'C:\\Users\\yfjin\\.hcss\\lstore\\1342220914\\'
#dir = 'C:\\Users\\yfjin\\.hcss\\lstore\\1342186275\\'
obs = getObservation(obsid, poolLocation=dir)
"""
############# now you can extract the frames at level 0 ########################
 extract the frames from the observation context "obs" """
if camera=='blue':
  frames=obs.level0.refs["HPPAVGB"].product.refs[0].product
elif camera=='red':
  frames=obs.level0.refs["HPPAVGR"].product.refs[0].product

""" Is it a Solar System Object ? """
sso = isSolarSystemObject(obs)

""" Attach pointing product to observation context """

pp = obs.auxiliary.pointing
"""
 get the calTree for this observation. The calTree contains all the calibration
 files needed for the data processing. The setting "time=frames.startDate" 
 ensures that the correct calibration files are attached to your observation.
 In particular, the SIAM calibration file which is necessary for the pointing
 calibration changed with time. The "date" of the observation is needed to
 attach the proper SIAM to the data for the correct pointing calibration.
"""

calTree = getCalTree(time=frames.startDate)

""" extract housekeeping parameters """

photHK=obs.level0.refs["HPPHK"].product.refs[0].product["HPPHKS"]

""" orbit ephemeris for the correct aberration correction when calculating
 the astrometry """

oep = obs.auxiliary.orbitEphemeris

"""
################################################################################
########################## Level 0 -> Level 0.5 ################################
################################################################################

 This little section of the script collects all the tasks you need to go from
 Level 0 up to Level 0.5. The tasks do not need any interaction by the user.
 These tasks need in input data taken from several auxiliary products. After
 this section the auxiliary products are not needed for the further data
 processing. Thus, before saving the frames in fits files for future
 re-processing, we recommend to reach at least Level 0.5. It is recommended
 to perform also this part of the data reduction to check whether the
 calibration block is properly removed or if the user might need to update
 the bad pixels table by flagging additional pixels.
"""

""" Filter the slew to target from the data """
frames = filterSlew(frames)

""" identify blocks in the observation. This task create a table (block table)
where the user can check the structure of the observation."""
frames = findBlocks(frames, calTree=calTree)

""" remove the calibration block and keep only the science frames."""
frames = detectCalibrationBlock(frames)
frames = removeCalBlocks(frames,useBbid=1)
#
frames = photFlagBadPixels(frames, calTree=calTree)
"""
 In the case you have your own bad pixel mask and you want tro insert it in
 the calTree, you can define your own calTree (mycal) in the way shown below.
 Please, uncomment the following four lines of code if you want to do that.
"""
#mycal=getCalTree()
#fa=FitsArchive()
#bad_pixel_prod=fa.load("my_own_bad_pixel_mask.fits")
#mycal.photometer.badPixelMask=bad_pixel_prod
"""
 The product bad_pixel_prod, defined above, contains the bad pixel mask you
 want to use. The last line put this mask in the bad pixel mask of your
 calTree mycal. If you want to use this mask in the photFlagBadPixels
 task, you have simply to call the task by giving in input your own calTree,
 as in the following example:
"""
#frames = photFlagBadPixels(frames, calTree=mycal) Below we show also

"""
 The phenomenon of electronic crosstalk was identified, in particular in the
 red bolometer (column 0 of any bolometer subarray), during the testing phase 
 and it is still present in in-flight data. We reccommend to flag those pixels
 in order to remove artifacts  from your map. To flag those pixels you need
 to read the BadPixel table and set the column zero to "True". You have then
 to save the modified BadPixel mask in a new calibration product  in your own
 "mycal" and use  this new calibration tree when calling the photFlagBadPixels
 task.
"""
frames = photMaskCrosstalk(frames)
""" flag saturated pixels """  
frames = photFlagSaturation(frames, calTree=calTree, hkdata=photHK)
#
""" convert from ADUs to Volts """
frames = photConvDigit2Volts(frames, calTree=calTree)
#
""" convert chopper angles into angles on the sky """
frames = convertChopper2Angle(frames, calTree=calTree)
#
""" compute the coordinates for the reference pixel (detector centre) with
 aberration correction. """
frames = photAddInstantPointing(frames,pp,orbitEphem = oep, calTree=calTree)
#
"""
 In case you object is a Solar system object, the following task moves SSO
 target to a fixed position in sky. This is needed for the mapping task.
"""
if (sso) :
  horizonsProduct = obs.auxiliary.horizons
  frames = correctRaDec4Sso (frames , timeOffset= 0, orbitEphem=oep, horizonsProduct=horizonsProduct, linear=0 )
#
"""
at this stage the auxiliary products can be deleted since they will not be
used in the further processing
"""

del pp
del photHK
del oep

"""
 At this point you can safely save the Level 0.5 frames in fits files, since
 the auxiliary products are not needed in  the further data processing. Here
 we propose a very simple output file name convention based on the obsid number
 and the channel (camera). You can choose to change the proposed name 
 convention in your favorite way. In this case, pay attention  to edit also
 the parts of the scripts where the files are read back to continue the data
 processing. 
"""
savefile = direc+"frame_"+"_" + str(obsid) + "_" + camera + "Level_0.5.fits"
simpleFitsWriter(frames,savefile)

"""
########################### END OF SECTION 1 ###################################
#
#
############################### SECTION 2 ######################################
################################################################################
######### IF YOU HAVE ALREADY SAVED THE LEVEL 0.5 PRODUCT START FROM HERE ######
################################################################################


 If you already saved the Level 0.5 data in fits files and you want to start
 from here the data redcution, uncomment the following three lines and comment
 the entire SECTION 1. Please, edit the savefile variable if you chose a
 different outout file name convention.
"""
#savefile = direc+"frame_"+"_" + str(obsid) + "_" + camera + "Level_0.5.fits"
#frames=simpleFitsReader(savefile)
#calTree = getCalTree(time=frames.startDate)
#
"""
 In the deep-survey case or in the case of a mini scam map with a point source
 the MMT method works pretty well without using an enormous amount of memory
 as for the  IIndLevelDeglitchTask and without being so time consuming as the 
 MapDeglitchTask. so our suggestion is always to try first with the MMT 
 method especially if you are reducing long observations. We provide here the
 parameters that are found to work generally well for this specific scientific
 case. We also provide few tricks that the user migths want to try in case of
 problem.
"""
frames = photMMTDeglitching(frames, incr_fact=2,mmt_mode='multiply', scales=3, nsigma=5)

"""
 A TIP: if the map contains few relatively bright sources, the task can
 misidentifies those sources as glitches. You can verify this case by looking
 at the coverage of the Level 2 map produced by the pipeline which uses the
 same parameter settings. If the MMT task deglitches on source, you will find
 holes at the position of the source peaks in the coverage map. There are
 several tricks to solve this problem.

 trick n. 1) you can provide the MMT task a "source mask" which let the task
 know where the sources are to avoid deglitching on source. You can obtained
 this mask with the same method described below for creating the high-pass
 filter mask but with a somewhat higher cut level in order to mask only bright
 sources. Then, you need, first, to read the fits file containing the source
 mask if such mask is not stored in memory
"""

#source_mask=simpleFitsReader("file_name_of_source_mask.fits")
""" 
  and provide an additional input when calling the task:
"""

#frames = photMMTDeglitching(frames, incr_fact=2,mmt_mode='multiply', scales=3, nsigma=5, sourcemask=source_mask)
"""
 You can then run once again the task with different "relaxed" parameters to
 flag also the glitches on source. If you do not change the name of the mask
 created by the MMT task, the mask will be updated by adding the newly
 detected glitches. If you prefer to keep the two masks separated you can
 change the name of the mask by adding the additional input
 maskname="new_mask_name" when calling photMMTDeglitching. You can, then,
 re-run the task with new and less stringent parameters to deglitch also the
 sources without damage"""

#frames = photMMTDeglitching(frames,scales=2,nsigma=9,mmt_mode='multiply',incr_fact=2)
"""
 trick n. 2) use the IILevel deglitching pefore projection (line...)
"""

"""
 You may want to check the masks created so far with the MaskViewer
"""
#from herschel.pacs.signal import MaskViewer
#MaskViewer(frames)

"""
 A TIP: another way (a bit time consuming but very useful) to check the mask
 is to project it as an image to see which regions of the real map are masked.
 This is very useful if you have a preliminary map and you can check whether
 real sources are systematically deglitched. To do this exercise we copy the
 frames in a new frames (frames_masked) and replace its signal with the mask
 values. We remove the considered mask (MMT_GlitchMask) from the frames to
 unmask the signal (otherwise you will get an empty map!) and project.
"""
#frames_masked = frames.copy()
#objectMask = frames_masked.getMask('MMT_Glitchmask').copy()
#frames_masked.setSignal(Double3d(objectMask))
#frames_masked = deactivateMasks(frames_masked,String1d(['MMT_Glitchmask']))
#map_mask = photProject(frames_masked,calTree=calTree)
#Display(map_mask)
"""you might delete the frames_masked and the map_mask after the check"""
#del(frames_masked,map_mask,objectMask)
#
#
""" apply the flat-field and convert Volts into Jy/pixel """
frames = photRespFlatfieldCorrection(frames, calTree = calTree)
#
""" assign ra/dec to every pixel. This is not necessary for the further data
 reduction and it increases the data volume by a factor 3. """
#frames = photAssignRaDec(frames, calTree=calTree)
"""
################################################################################
######################### SAVING the LEVEL 1 PRODUCT ###########################

 At this point you got to the Level 1 product, which is calibrated from most
 of the instrumental effects. You might want to save this product before the
 highpass filter task to be able to go back and optimize your data redcution.
 The script stores locally your data as a fits file in the output directory
 "direc" specified above. We propose here the same name convention used for
 saving the Level 0.5 products.
"""
savefile = direc+"frame_"+"_" + str(obsid) + "_" + camera + "Level_1.fits"
simpleFitsWriter(frames,savefile)
#
"""
########################## END OF SECTION 2 ####################################

############################# SECTION 3 ########################################
################################################################################
######################### Level 1 -> Level 2 ###################################
################################################################################

 If you saved the Level 1 products and whish to start from here the data
 processing, then comment or delete the SECTION 1 and 2 of this script and
 uncomment the following three lines of code. The script assumes you saved
 the Level 1 product with the name convention suggested above. Please change
 the savefile variable if you used a different convention. 
"""
#savefile = direc+"frame_"+"_" + str(obsid) + "_" + camera + "Level_1.fits"
#frames=simpleFitsReader(savefile)
#calTree = getCalTree(time=frames.startDate)
"""
################################     MASKING      ##############################
 Now we get to the crucial point. This script shows how to reduce the data via
 the high-pass filtering + PhotProject method. The high-pass filtering task
 removes from the signal a median calculated within a given box around each
 readout in the timeline. This means that if the sources are not properly
 masked, also the source signal can be removed by this task. Thus, masking
 means providing to the high-pass filtering task the information on the
 location of the sources on the timeline, to let the task calculate the median
 only with readouts that are not classified as "source" in the mask. This
 scripts provides here several options, suggestions and tricks that the
 user might want to try to optimize the data reduction for her/his own
 observation.

 option = 1
 If your scientific case is a deep survey of a blank field, your sources will
 not be detectable on the single obsid map due to the low S/N. We suggest to
 perform  a preliminary reduction without masking any source. You need to
 reduce all obsid, combine the individual maps and base the mask on a first
 preliminary mosaic (see the multiple_obsid_scanmap_Deep_survey_miniscan_
 Pointsource.py script for the details how to make the mosaic). Although the
 preliminary map will show strong high-pass filtering residuals, you can use it
 to obtain a good mask of the sources. You can, then, reduce once again the
 individual obsid by using the mask based on the much deeper mosaic. This
 option offers to use a "unmasked" high-pass filtering for obtaining a
 preliminary map for building the mosaic.
 

 option = 2
 If the user has already a mask derived from a preexisting map at different
 wavelength or from a preliminary reduction, then she/he needs only to attach
 to the frames the desired mask via a dedicated task, run then the high-pass
 filtering and the projection tasks.

 option = 3
 An alternative way to create the mask in the case of a deep field plenty of
 point sources, is to provide a prior catalog with sky coordinates and 
 put a circular patch of a given radius at any position. This can be done via
 a dedicated task by providing directly a list of coordinates or an ascii file
 containing a catalog of coordinates and by specifying the radius of the 
 circular patch.

 In all the considered cases the mask used to masking the sources is called 
 "HighpassMask" throughout the script

############################### FIRST OPTION option = 1 ########################
"""
if option == 1:
  """
   In this option the high-pass filter is used without masking any source. 
   USE THIS OPTION ONLY FOR A PRELIMINARY DATA REDUCTION TO OBTAIN A FIRST 
   MOSAIC TO GET THE MASK.

   A TIP: for this particular usage of the highpassFilter task, we suggest
   to use a relatively large hp width in order to limit the damages of the
   sources. A smaller hp width can be used for the defnitive reduction when
   the highpassFilter is used with a mask.
  """
  frames  = highpassFilter(frames,hpfradius)
  #
elif option == 2:
  """
  ######################### SECOND OPTION option = 2 ###########################
   In this option the script assumes the user has already a mask called 
   HighpassMask. The file containing the mask is loaded as "maskfile"
  """
  mask=simpleFitsReader(maskfile)
  """
   the following task attaches the mask to the frames.
  """
  frames  = photReadMaskFromImage(frames, si=mask, extendedMasking=True,maskname="HighpassMask")
  """
   A TIP: in many cases the MMT deglitch mights detect very bright sources as 
   glitches. If this is your case and you did not use any of the tricks 
   suggested above, it is often useful to disable the deglitching on target. 
   To do that you can use the 'HighpassMask' which provides information on the 
   source location.
  """
  #maskMMT=frames.getMask('MMT_Glitchmask')
  #maskHPF=frames.getMask('HighpassMask')
  #frames.setMask('MMT_Glitchmask',maskMMT & (maskHPF == 0))
  """
   Running the "masked" high-pass filtering.
   AN IMPORTANT TIP: HOW TO SET THE HPFRADIUS: if the hpfradius is smaller than 
   the source size (the FWHM of the PSF in case of point sources), the whole 
   hpfradius could be masked. In this case the task will calculate the median
   over the given hpfradius without considering the mask,thus removing also the 
   source flux. In this case the "interpolateMaskedValues" parameter should be
   set to True to let the task interpolate between the closest values of the 
   median over the timeline. The hpfradius is set in SECTION 0, where we put 
   all the settings. The default parameter is 15 readouts for the blue channel 
   and 25 for the red channel. This value is usually adopted in the case of 
   deep surveys with medium speed of 20"/s. Thus, the 15 readouts used in the 
   blue channel correspond to a radius of 30", and the 25 readouts used in the 
   red channel to a radius of 50". Extensive analysis on the effects of the 
   high-pass filtering on the PSF have shown that these values of the hpfradius 
   allow to remove most of the 1/f noise without damaging the PSF. Indeed, the 
   effect is to remove part of the exetrnal lobes of the PSF without affecting 
   the PSF core, where 95% of the light is enclosed. Smaller hpfradius would 
   remove also part of the flux in the core of the psf. Thus, we suggest to not 
   use smaller values than those proposed here. If the observation is performed 
   at lower speed (10 "/s) or the source is particularly big or bright, you are 
   invited to enlarge the hpfradius to be as large and the source size. In 
   the high speed case (60 "/s) the hpradius can be reduced to 8 readouts in 
   blue channel and 15 in the red.
   We do not reccommand values larger than 100 and 150 readouts in the blue 
   and red channel, respectivly, since this would not allow to properly remove 
   the 1/f noise. 
  """
  frames  = highpassFilter(frames,hpfradius,maskname="HighpassMask", interpolateMaskedValues=True)
  #
  #
elif option == 3:
  """
  ############################################# THIRD OPTION option = 3 ############################################################
  In this option the script assumes the user provides an ascii file with a list
  of sky coordinates to create a mask with circular patches of a given radius 
  (specified by the user) at the given coordinates. The radius of the circular
  patches should be as large as the FWHM of the PSF to limit the damages due to
  the highpassFiletr task. The radius provided to MaskFromCatalogueTask task
  must be a 1d array. In this way the user has the possibility to specify 
  different radii for different sources. This is particularly useful if the 
  deep field contains few slightly extended sources (nearby galaxies). If 
  radius contains just one value, that is used for all sources of the prior 
  catalog. The radius is expressed in arcsec.
  """
  if input_setting==False: 
     file='sky_coordinates.txt'
     ascii=AsciiTableTool()
     ascii.template=TableTemplate(2,names=["ra","dec"],types=["Double","Double"])
     ascii.parser=FixedWidthParser(sizes=[10,10])
     table=ascii.load(file)
     radius=Double1d(1)
     radius[0]=9.0
     """ 
      if you want to specify a differnt radius for each suurce, load, instead,
      a catalog with the following format
     """
     #ascii.template=TableTemplate(3,names=["ra","dec","radius"],types=["Double","Double","Double"])
     #ascii.parser=FixedWidthParser(sizes=[10,10,4])
     """ the previous line specifies the format of the catalog. Please, edit the
     line to specify your own format.
     """
     #
     ra=table["ra"].data
     dec=table["dec"].data
  #
  """
  The task needs in input also a map with the correct WCS. For this purpose
  we use the map Level2 product taken from the observation context.
  """
  map=obs.refs["level2"].product.refs["HPPPMAPR"].product
  from herschel.pacs.spg.phot import MaskFromCatalogueTask
  mfc = MaskFromCatalogueTask()
  mask = mfc(map, ra, dec, radius, copy = 1)
  """
   the following task attaches the mask to the frames.
  """
  frames  = photReadMaskFromImage(frames, si=mask, extendedMasking=True,maskname="HighpassMask")
  """
  running masked high-pass filter
  """
  frames  = highpassFilter(frames,hpfradius,maskname="HighpassMask", interpolateMaskedValues=True)
"""
################################################################################
######################### END OF MASKING & HP OPTION ###########################
################################################################################
"""
  
"""  
   Next command selects only frames for which the telescope is slewing at a
   constant speed, i.e. remove the turnaround loops between scan legs. This
   is done by removing all readouts at a velocity 10% higher or lower than the
   scan speed (limit=10)

"""
#
frames= filterOnScanSpeed(frames,limit=10)

"""
 If you did not execute the deglitching via MMT, you need to do it at this
 stage before the final projection. There are two possibilities. The former,
 IIndLevelDeglitchTask, mights need a large use of RAM. In case you are
 reducing a long observation, this can become a serious problem.  If this is
 the case of your data processing, you might want to try a similar method,
 which uses a significant smaller amount of memory, but it is more time-
 consuming. This alternative task is called MapDeglitchTask and is similar in
 concept to the IIndLevelDeglitchTask. The main difference between the two
 tasks is that MapDeglitchTask does not store information in memory, thus,
 reducing the need of memory. The commands needed to call this task are listed
 below. We suggest to use a nsigma parameter equal to 30 for an effective
 deglicthing. 

 IMPORTANT NOTE: be aware that for executing the MapDeglitchTask task there is
 no need to execute MapIndexTask task.
"""
#from herschel.pacs.spg.phot.deglitching.map import MapDeglitchTask
#s = Sigclip(nsigma=30,behavior="clip",outliers="both",mode=Sigclip.MEDIAN)
#mdt = MapDeglitchTask()
#
#deg = mdt(frames,deglitchvector='timeordered',maskname='SecondGlitchmask',algo=s)
#
"""
######################### finally the projection ###############################

 The photProject task performs a simple coaddition of images, by using the
 drizzle method (Fruchter and Hook, 2002,PASP, 114, 144). There is not
 particular treatment of the signal in terms of noise removal. The 1/f noise
 is supposed to be removed by the high-pass filtering task. The key parameters
 of this task are the the output pixel size and the drop size. A small drop
 size can help in reducing the cross correlated noise due to the projection
 itself (see for a quantitative treatment the appendix in Casertano et al.
 2000, AJ, 120,2747). Please, remember that the remaining 1/f noise not removed
 by the high-pass filter task is still a source of cross-correlated noise in
 the map. Thus, the formulas provided by Casertano et al. 2000, which account
 only for the cross correlated noise due to the projection, do not provide a
 real estimate of the total cross correlated noise of the final map. Indeed,
 this is a function of the high-pass  filter radius, the output pixel and the
 drop size.  Nevertheless, those formulas can be  used to reduce as much as
 possible the cross-correlated noise due to the projection. We stress here
 that the values of output pixel size and drop size strongly depend on the
 redundancy of the data (e.g. the repetition factor). For instance, a too
 small drop size would create holes in the final map if the redundancy is not
 high enough (see Fruchter and Hook, 2002 and the PDRG for a clear explanation).
 The values proposed here for the output pixel and drop size are intended to
 be optimal for a standard mini scan map. The output pixel size is given by
 the outpixsz variable set in the SECTION 0. We set the output pixel size to
 2 and 3 arcsec for the blue and the red channel, respectively. The drop size
 is set in the pixfrac parameter in the photProject input. The pixfrac
 parameter is expressed as the ratio between the drop and in input pixel size.
 A drop size of 1/10 the input pixel size is found to give very good quality
 in the final map. Since these parameters have to be adjusted case by case,
 we invite you to play with them to find the right balance between noise,
 cross-correlated noise and S/N of the source for creating the optimal map.
"""
map=photProject(frames, outputPixelsize=outpixsz, calTree=calTree, pixfrac=pixfrac)

"""
 The photProject task comes in two flavors: a simple average of the input
 pixel contributions to the given output pixel as done in the previous line,
 or a weighted mean of those contributions. The weights are estimated as the
 inverse of the error square.  However, since the noise propagation is not
 properly done in the PACS pipeline a proper error cube must be provided to
 obtain good maps. We stress here that this method can not relay on the errors
 provided by the pipeline. We propose here a trick to estimate a reliable
 error cube to perform the weighted mean. HOWEVER, BE AWARE THAT THIS TRICK
 IS WORKING ONLY WHEN THE BACKGROUND NOISE IS DOMINATING, AS FOR THE DEEP
 SURVEY CASE. FOR THE MINI SCAN MAP CASE, BE AWARE THAT IF YOU ARE OBSERVING
 A BRIGHT SOURCE, THIS METHOD IS NOT RECOMMENDED SINCE AT THIS STAGE OF THE
 DATA REDUCTION THE BRIGHT SOURCE CAN DOMINATE THE BACKGROUND. Be also aware
 that the final noise map associated to the final map and based on this error
 cube is not meaningful. The error cube proposed here is intended to be used
 only for the estimate of the weights in the weighted mean of photProject. 

 The error for each readout is estimated as the stdev in a box as large as
 10 times the hpfradius centered on the readout along the timeline. To avoid
 the occurrence of NaNs, for readouts where the error is zero
 (e.g. no coverage) the error is set manually to 1.e6 to get negligible weights.
"""
#noisecube=Condense(2,10*hpfradius,STDDEV, "boxcar")(frames["Signal"].data)
#noisecube[noisecube.where(noisecube==0)] = 1e6
#frames.setNoise(noisecube)
"""
To perform the weighted mean the weightedsignal parameter has to be set to True. 
"""
#map=photProject(frames, outputPixelsize=outpixsz, calTree=calTree, weightedsignal=True, pixfrac=pixfrac)
#
"""
 A TIP: you might want to use a specific wcs for your final map. Here it is
 shown how to set the wcs parameters. The reference pixel is at the the center
 of the map. To set these parameters the user must have an idea of the map
 dimensions for the given output pixel size. We propose an automatic way to
 retrieve the center of the map from the metadata. However, you might want
 to check that on the Level 2 map provided by the automatic pipeline.
 Setting a fixed wcs could be very useful if your observation comprises many
 obsid and you want to produce maps all with the same wcs. Indeed, in this
 case you can combine the individual obsid maps easily to get the final map
 by just averaging or by taking a weighted mean (e.g. weighted by coverage)
 of the individual output pixels. In addition the standard deviation of the
 output pixel signal can provide a good estimate of the noise. In this way
 you can obtain a meaningful noise map associated to your final map, which
 is still not available as output of the current pipeline version. 
"""
#ra_reference=0.000       #provide here the map center ra in deg
#dec_reference=0.000    #provide here the map center dec in deg
#
# build wcs
#
#pixsize=outpixsz
#rad1=240    ##(half the dimension of the map in the x direction in pixel units)
#rad2=240    ##(half the dimension of the map in the y direction in pixel units)
#
#my_wcs=Wcs(cunit1="Degrees",cunit2="Degrees",cdelt1=-pixsize/3600.,\
#      cdelt2=pixsize/3600.,crota2=0.,crpix1=rad1,crpix2=rad2,\
#      crval1=ra_reference,crval2=dec_reference,ctype1="RA---TAN",ctype2="DEC--TAN",\
#      equinox=2000.0)
#my_wcs.setParameter("naxis1",2*rad1,"naxis1")
#my_wcs.setParameter("naxis2",2*rad2,"naxis2")
"""
 to set the wcs in photProject you need just to set the wcs parameter 
"""
#map=photProject(frames, outputPixelsize=outpixsz, calTree=calTree, weightedsignal=True, pixfrac=0.1,wcs=my_wcs)
"""
 display the map
"""

Display(map)
#
"""
 save the map as a FITS file :
"""
outfile = direc+ "map_"+"_" + str(obsid) + "_" + camera + ".fits"
print "Saving file: " + outfile
simpleFitsWriter(map,outfile)  


del frames
del obs
System.gc()
print "done:",obsid,camera

# ----------------------


endPipeline=time.clock()
TPipeline=endPipeline-beginPipeline
print TPipeline
Double1dNumCount.Double1dGetALL()
Double2dNumCount.Double2dGetALL()
Complex1dNumCount.Complex1dGetALL()
MatrixNumCount.MatrixGetALL()
FFTNumCount.FFTGetALL()
SVDNumCount.SVDGetALL()