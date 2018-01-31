import numpy as np
import matplotlib.pyplot as plt
import random as rand
import time_series as ts



Tmax = 10000
B1D = ts.time_series(Tmax)

Tx1, Xt1 = B1D.BrownianMotion_1D(1.0)
Tx2, Xt2 = B1D.BrownianMotion_1D(1.0)
Tx3, Xt3 = B1D.BrownianMotion_1D(1.0)

for n in range(100,2000,50):
    Tx2, Ma2 = B1D.moving_average(Tx2,Xt2,n)
    plt.plot(Tx2,Ma2,"-")

#plt.plot(Tx1,Xt1)
#plt.plot(Tx2,Xt2)
plt.plot(Tx2,Xt2)
plt.show()



