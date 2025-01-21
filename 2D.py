import numpy as np
import matplotlib.pyplot as plt
import math
import os
from timeit import default_timer as timer



a1=0.8839
a2=0.6267
Nx=400         # size of system (Nx=Ny)
Ny=400


U = np.zeros((Nx,Ny))           #the current array
dUdt = np.zeros((Nx,Ny))        #the array for store values of the next time

#-----------------------------       
              
    if ( t % printfreq == 0):
           
           # saving field data to files
          np.savetxt("{0}/Phi_ful_imp_ani{1}.csv".format(dir_path, t), Phi, delimiter=",")
          np.savetxt("{0}/U_ful_imp_ani{1}.csv".format(dir_path, t), U, delimiter=",")        
          print(t)

       
end = timer()
print("Completed time is %s" % (end-start))
        