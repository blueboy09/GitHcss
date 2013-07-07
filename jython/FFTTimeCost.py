# FFT Time Cost
Path="C:\\Users\\yfjin\\hcss\\workresult\\FFT\\"
OpsArray=["NCfft","NCifft"]
AllTime=0
for Ops in OpsArray:
    AllTime=AllTime+FFTTimeCost.TimeCost(Ops,Path)
    print AllTime
print "FFT Time Cost = ", AllTime
fp = open(Path+"result.txt",'w')
print >> fp,"FFT Time Cost = ", AllTime
fp.close()