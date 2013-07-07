# MatrixMultiply TimeUsed Calculate
Path="C:\\Users\\yfjin\\hcss\\workresult\\Double2d\\"
OptArray=[Double2dNumCount.Add1,Double2dNumCount.Add2,Double2dNumCount.Sub1,\
	Double2dNumCount.Sub2,Double2dNumCount.Mul1,Double2dNumCount.Mul2,\
	Double2dNumCount.Div1,Double2dNumCount.Div2,Double2dNumCount.DotProduct1,\
	Double2dNumCount.DotProduct2,Double2dNumCount.Pow,Double2dNumCount.Abs,\
	Double2dNumCount.Neg,Double2dNumCount.Mod]
TimeUsed={"Add1":0,"Add2":0,"Sub1":0,"Sub2":0,"Mul1":0,"Mul2":0,"Div1":0,"Div2":0,\
	"DotProduct1":0,"DotProduct2":0,"Pow":0,"Neg":0,"Abs":0,"Mod":0,}
timeList=[]
#MaTimeCost=MatrixTimeCost()
D2dTimeCost=Double2dTimeCost("Double2dTimeCost")
for Opt in OptArray :
    D2dtime=D2dTimeCost.TimeCost(Opt,Opt._name,Path)
    timeList.append(D2dtime)
    D2dTimeUsed[Opt._name]=D2dtime

print "Double2d Time Cost = ", timeList

fp = open(Path+"result.txt",'w')
print >> fp, "Double2d Time Cost = ", timeList
fp.close()



