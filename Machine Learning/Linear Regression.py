import numpy as np 
import matplotlib.pyplot as plt 

def estimate_coef(x, y):

	#No. of observation Points
	n = np.size(x)

    #Mean of x and y Vector
	m_x, m_y = np.mean(x), np.mean(y)
     
    #calculating cross-deviation and deviation about x
    SS_xy = np.sum(x * y) -n*m_y, m_x
