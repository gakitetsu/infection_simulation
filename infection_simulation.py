import numpy as np
import matplotlib.pyplot as plt

S = 1000000
I = 100
R = 0
N = S + I + R
m = 20
p = 0.02

beta = m * p / N
gamma = 1.0 / 14 

S_arr = []
I_arr = []
R_arr = []
cnt = 0

while cnt < 300:

    delta_S = -beta * S * I
    delta_R = gamma * I
    delta_I = -delta_S - delta_R
    
    S += delta_S
    I += delta_I
    R += delta_R
    
    S_arr.append(S)
    I_arr.append(I)
    R_arr.append(R)
    cnt = cnt + 1
    
plt.plot(range(cnt), S_arr)
plt.plot(range(cnt), I_arr)
plt.plot(range(cnt), R_arr)

plt.show()
