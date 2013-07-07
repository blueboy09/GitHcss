toy: this part is a toy to quick start jcuda application in HIPE.
Our application involve some double-precision which is not sopport by all CUDA GPU except whose compute capability higher than 1.3. Here, we only care about how to use jcuda in HIPE. So, we use a toy application that only support float-precision matrix multiply which most Nvidia GPU support.

The steps to use:

0. Install Nvidia GPU driver and CUDA 5.0

1. Download Jcuda, configure the system environment varible "PATH" and "CLASSPATH".
The JAR files have to be present in the CLASSPATH, and the native library files must be located in a path that is visible for Java. In most cases, this should either be a path that is given as a java.library.path for the JVM, or the root directory of the project. (Alternatively, they can also be in a path that is contained in an environment variable like the PATH environment variable on Windows or the LD_LIBRARY_PATH environment variable on Linux)

2. Replace the corresponding jar file in your hipe repository using the new one with Jcuda application.
(note: if you don't care about how to write source modify by yourself, you can go to step 2.3 directly)

	2.1 Configure you eclipse. (see http://herschel.esac.esa.int/twiki/bin/view/Hcss/DeveloperGuide). Install a new CVS project. The source you can download from 	hercvs01.esac.esa.int:2401/services/repositories/HERSCHEL_CVS. For the toy, we build a "ia.numeric.toolbox.matrix" class. Then build a new java class 	MatrixMultiplyToy, the source you can find in "ia.numeric.toolbox.matrix.src.zip" in this directory. Finally, add "MatrixMultiplyToy" in the __all__ list in 	the __init__ file.

	2.2 right click the project "ia.numeric.toolbox.matrix" in the package explore window. Select "Export" and export the jar file. 

	2.3 Replace the crresponding jar file in your own hipe repository by the jar file your export just now.(if you don't do the step 2.1 and 2.2, you can use the 	jar file in this direcroty to replace because of portability of java). 

	2.4 Restart HIPE.bat and try the script:

		A = Int2d([[1,2,3], [2,3,4]])
		B = Int2d([[1,2], [2,3], [3,4]])
		X = Float2d([[1,2,3], [2,3,4]])
		Y = Float2d([[1,2], [2,3], [3,4]])
      
		print A.apply(MatrixMultiplyToy(B))
	      	#if the result is [[14,20],[20,29]], then it means your jar file is replaced right.
		
		MatrixMultiplyToy.SetGPU(True)
		print X.apply(MatrixMultiplyToy(Y))
	      	#if the result if [[14.0£¬20.0]£¬[20.0,29.0]], then it means jcuda configure right and you can use it in your HIPE.

