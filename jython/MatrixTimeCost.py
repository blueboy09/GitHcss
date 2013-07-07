# MatrixMultiply TimeUsed Calculate
Path="C:\\Users\\yfjin\\hcss\\workresult\\Matrix\\"
OptArray=[MatrixNumCount.Bool1,MatrixNumCount.Bool2,MatrixNumCount.Byte1,MatrixNumCount.Byte2,\
	MatrixNumCount.Short1,MatrixNumCount.Short2,MatrixNumCount.Int1,MatrixNumCount.Int2,\
	MatrixNumCount.Long1,MatrixNumCount.Long2,MatrixNumCount.Float1,MatrixNumCount.Float2,\
	MatrixNumCount.Double1,MatrixNumCount.Double2]
MaTimeUsed={"Bool1":0,"Bool2":0,"Byte1":0,"Byte2":0,"Short1":0,"Short2":0,\
	"Int1":0,"Int2":0,"Long1":0,"Long2":0,"Float1":0,"Float2":0,"Double1":0,"Double2":0}
timeList=[]
#MaTimeCost=MatrixTimeCost()
MaTimeCost=MatrixTimeCost("MatrixTimeCost")
for Opt in OptArray :

    Matime=MaTimeCost.TimeCost(Opt,Opt._name,Path)
    timeList.append(Matime)
    MaTimeUsed[Opt._name]=Matime

print "Matrix Multiply Time Cost = ", timeList

fp = open(Path+"result.txt",'w')
print >> fp, "Matrix Multiply Time Cost = ", timeList
fp.close()