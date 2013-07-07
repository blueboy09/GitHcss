# SVD time cost 
Path="C:\\Users\\yfjin\\hcss\\workresult\\SVD\\"
OpsArray=["SVDF1","SVDF2","SVDD1","SVDD2"]

svdd=SVDNumCount.SVDNcInput(SVDNumCount.SVDD1,Path)
svdd=Long2d(svdd)
#print svdd

import time
timeBegin=time.clock()
AllTime=0
for Ops in OpsArray:
    AllTime=AllTime+SVDTimeCost().TimeCost(Ops,Path)

print AllTime
timeEnd=time.clock()-timeBegin
print "SVD Time Cost = ", timeEnd
fp = open(Path+"result.txt",'w')
print >> fp, "SVD Time Cost = ", timeEnd
fp.close()