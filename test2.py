import numpy as np
import matplotlib.pyplot as plt
import random as rand
import time_series as ts


Tmax = 500

order = 2
phi_vec = [0.1,0.1]
mu = 1.0
sigma = 1.0
MA_1 =  ts.Moving_average(mu,sigma,phi_vec,order,Tmax)

order = 2
phi_vec = [-0.0,0.8]
mu = 1.0
sigma = 1.0
AR_1 =  ts.Auto_regressive(mu,sigma,phi_vec,order,Tmax)

Tx1,Xt1 = MA_1.MA_model()
Tx2,Xt2 = AR_1.AR_model()

plt.plot(Tx1,Xt1)
plt.plot(Tx2,Xt2)

plt.show()
