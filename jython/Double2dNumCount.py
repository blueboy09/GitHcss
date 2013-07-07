Path="C:\\Users\\yfjin\\hcss\\workresult\\Double2d\\"

Double2dNumCount.Double2dGetALL()
OptArray=[Double2dNumCount.Add1,Double2dNumCount.Add2,Double2dNumCount.Sub1,Double2dNumCount.Sub2,\
	Double2dNumCount.Mul1,Double2dNumCount.Mul2,Double2dNumCount.Div1,Double2dNumCount.Div2,\
	Double2dNumCount.Abs,Double2dNumCount.Pow,Double2dNumCount.Mod,Double2dNumCount.Neg,\
	Double2dNumCount.DotProduct1,Double2dNumCount.DotProduct2]
for Opt in OptArray:
    Double2dNumCount.Double2dNcOutput(Opt,Opt._name,Path)
