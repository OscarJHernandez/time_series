import numpy as np
import random as rand
#
# Author: Oscar Javier Hernandez
#


class time_series:
    
    
    def __init__(self,Tmax):
        self.Tmax = Tmax # The maximum number of time steps in the simulation
    
    
    
    # Simulate Brownian motion in one 
    def BrownianMotion_1D(self,dx):
        
        X=[]
        T=[]
        xtm1 = 0.0
        xt = 0.0
        
        for t in range(0,self.Tmax):
            
            u = rand.random() 
            
            X.append(xt)
            T.append(t)
            
            if(u>0.5):
                xt = xtm1 + dx
            else:
                xt = xtm1 - dx
            
            xtm1 = xt 
        
        
        X = np.asarray(X)
        T = np.asarray(T)
        
        return T,X
    
    
    # Calculate the moving Average of a Process
    # mA(n,tk) = (xk+xk-1+...+xk-n)/n
    def moving_average(self,T,X,n):
        mA = []
        
        for k in range(0,n):
            mA.append(0.0)
        
        for k in range(n,len(X)):
            ma_k = sum(X[k-n:k])/float(n)
            mA.append(ma_k)
        
        
        mA = np.asarray(mA)
        
        return T,mA
        
