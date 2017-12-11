# Sellar
Optimization of Sellar Problem in Python

This script has been developed and tested in Python 2.7.0.

Before running the scripts, make sure the following packages are installed
1. openopt
2. FuncDesigner

Once you have installed the packages, execute the main.py script. The output is printed below:




Initial Objective: 28.588308496
[x1 z1 z2] = [1, 5, 2]
[y1 y2] = [25.5883027008, 12.0584881833]

------------------------- OpenOpt 0.5625 -------------------------
problem: unnamed   type: NLP    goal: minimum
solver: scipy_cobyla
  iter  objFunVal  log10(maxResidual)  
    0  2.859e+01            -100.00 
   10  3.183e+00              -9.27 
istop: 1000
Solver:   Time Elapsed = 0.0 	CPU Time Elapsed = 0.01
objFuncValue: 3.1833939 (feasible, MaxResidual = 5.40728e-10)

--------------------------------------------------
Final Objective: 3.18339394914
[x1 z1 z2] = [  3.38813179e-21   1.97763897e+00   0.00000000e+00]
[y1 y2] = [3.15999999946, 3.75527785062]
