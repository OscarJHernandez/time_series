import numpy as np
import random as rand
#
# Author: Oscar Javier Hernandez
#


class Time_series:
    
    
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
        
    #
    # The sample mean of a time series, average of the last n-points
    #
    def sample_mean(self,X,n):
        
        ma_n = sum(X[len(X)-n:len(X)])/float(n)
        
        return ma_n
        
        
#===============================================================================================
#
# MA(q) = mu + eps_t + eps_{t-1}*Phi_1 + eps_{t-2}*Phi_2 + ... + eps_{t-q}*Phi_q
#
# eps ~ N(0,sigma**2)
#        
#===============================================================================================
class Moving_average(Time_series):
    
    # The constructor of the subclass
    # We initialize the  
    def __init__(self,mu,sigma,phi_vec,order,Tmax):
        
        self.mu = mu
        
        self.sigma = sigma
        
        self.Tmax = Tmax # Feed the Tmax value
        
        self.order = order # The order of the moving average model
        
        self.phi_vec = np.append([1.0], phi_vec) # Initialize the parameters of the model
        
    
    #----------------------------------------------------------------------
    #
    # This function generates data from the MA model
    #
    #----------------------------------------------------------------------
    def MA_model(self):
        
        T = []
        mA = []
        
        n = self.order
        
        eps = np.zeros(n)
        
        sigma = self.sigma
        
        mu = self.mu
        
        
        for t in range(0,self.Tmax):
            
            eps0 = np.random.normal(0.0, sigma)
            
            # Store all random numers in a growing array
            eps = np.append(eps,eps0)
            
            # Store a subset of the epsilon array
            eps_vec = eps[-n-1:]
            
            # Reverse the order
            eps_vec = eps_vec[::-1]
            
            # For debugging purpuses
            #print eps0
            #print eps_vec
            #print self.phi_vec
            #print ""
            
            eps_dot_phi = np.dot(eps_vec,self.phi_vec)
            
            mA_t = mu + eps_dot_phi
            
            T.append(t)
            mA.append(mA_t)
        
       
        T = np.asarray(T)
        mA = np.asarray(mA)
        
        return T,mA
        


# auto-regressive model
#===============================================================================================
#
# MA(q) = mu + eps_t + X_{t-1}*Phi_1 + X_{t-2}*Phi_2 + ... + X_{t-q}*Phi_q
#        
#===============================================================================================
class Auto_regressive(Time_series): 
    
    
        # The constructor of the subclass
    # We initialize the  
    def __init__(self,mu,sigma,phi_vec,order,Tmax):
        
        self.mu = mu
        
        self.sigma = sigma
        
        self.Tmax = Tmax # Feed the Tmax value
        
        self.order = order # The order of the Autoregressive model
        
        self.phi_vec = phi_vec
    
    #----------------------------------------------------------------------
    #
    # This function generates data from the Auto Regressive model
    #
    #----------------------------------------------------------------------
    def AR_model(self):
        
        n = self.order
        
        T = np.zeros(n)
        X = np.zeros(n)
        
        sigma = self.sigma
        
        mu = self.mu
        
        
        for t in range(0,self.Tmax):
            
            # Store a subset of the epsilon array
            X_vec = X[-n:]
            
            # Reverse the order
            X_vec = X_vec[::-1]
            
            # For debugging purpuses
            #print eps0
            #print eps_vec
            #print self.phi_vec
            #print ""
            
            X_dot_phi = np.dot(X_vec,self.phi_vec)
            
            # Generate a new random number
            eps0 = np.random.normal(0.0, sigma)
            
            xt = mu +eps0+ X_dot_phi
            
            T= np.append(T,t)
            X= np.append(X,xt)

        

        return T,X
        
             
        
        
