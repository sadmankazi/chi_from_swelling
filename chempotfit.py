
import numpy as np 
from scipy.optimize import curve_fit 
  
from matplotlib import pyplot as plt 
  
import os 
import sys

os.chdir(sys.path[0])


x = np.array([0.005, 0.01, 0.0125, 0.015, 0.016, 0.02, 0.021, 0.022]) # water fraction in film 
y = np.array([0.3,   0.44, 0.5,    0.7,  0.73,  0.9, 0.92, 0.95]) # water activity  

# Test function with coefficients as parameters 
def func(x, chi): 
    return np.exp((1-x) + np.log(x) + chi * (1-x)**2)
  
 
param, param_cov = curve_fit(func, x, y) 
  
  
print("Chi:") 
print(param) 
# print("Covariance of coefficients:") 
# print(param_cov) 
  
# fit stores the new y-data according to  
# the coefficients given by curve-fit() function 
fit = np.exp((1-x) + np.log(x) + param[0] * (1-x)**2)

plt.plot(x, y, 'o', color ='red', label ="data") 
plt.plot(x, fit, '--', color ='blue', label ="Fit $\chi$ = {}".format(np.round(param[0],2))) 
plt.xlabel('$\phi_w$')
plt.ylabel('Vapor activity')
plt.legend(frameon = False) 
plt.show() 