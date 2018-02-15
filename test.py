import numpy as np
import matplotlib.pyplot as plt
import random as rand
import time_series as ts



Tmax = 50
B1D = ts.Time_series(Tmax)

Tx1, Xt1 = B1D.BrownianMotion_1D(1.0)
Tx2, Xt2 = B1D.BrownianMotion_1D(1.0)
Tx3, Xt3 = B1D.BrownianMotion_1D(1.0)


#plt.plot(Tx1,Xt1)
#plt.plot(Tx2,Xt2)
#plt.plot(Tx2,Xt2)
#plt.show()


order = 2
phi_vec = [0.0,0.0]
mu = 1.0
sigma = 1.0
MA_1 =  ts.Moving_average(mu,sigma,phi_vec,order,Tmax)

order = 3
phi_vec = [0.5,-0.5,0.5]
MA_2 =  ts.Moving_average(mu,sigma,phi_vec,order,Tmax)

Tx1,Xt1 = MA_1.MA_model()
Tx2,Xt2 = MA_2.MA_model()

print  MA_2.sample_mean(Xt1,5)

plt.plot(Tx1,Xt1)
plt.plot(Tx2,Xt2)

plt.show()
