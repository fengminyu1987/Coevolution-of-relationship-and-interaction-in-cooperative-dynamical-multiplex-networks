

import matplotlib.pyplot as plt
import numpy as np

c_heat=[[0.019348,0.026866,0.39646,0.85084399],
[0.023824,0.045958,0.57491,0.890096],
[0.023158,0.10816,0.68042,0.982452],
[0.03318,0.128174,0.703558,0.9228],
[0.050778,0.120582,0.727574,0.934794],
[0.052418,0.2498,0.74081,0.918826],
[0.033408,0.475218,0.733358,0.93],
[0.063636,0.633487,0.76684,0.92582],
[0.03838,0.671292,0.7655,1],
[0.0627,0.667334,0.770322,1],
[0.065,0.68452,0.779358,1]]

x = [0.5+0.05*i for i in range(len(c_heat))]
y=[]

for i in range(0,len(c_heat[0])):
    y0=[]
    for j in range(len(c_heat)):
        y0.append(c_heat[j][i])
    y.append(y0)





plt.figure(dpi=600)
plt.plot(x, y[0],marker='o',markersize=8, linewidth=2.5, label="HL", color='green', linestyle='-.')
plt.plot(x, y[1],marker='o',markersize=8, linewidth=2.5, label="SL", color='orange', linestyle='-.')
plt.plot(x, y[2],marker='o',markersize=8, linewidth=2.5, label="XL", color='dodgerblue', linestyle='-.')
plt.plot(x, y[3],marker='o',markersize=8, linewidth=2.5, label="WS", color='red', linestyle='-.')



#plt.plot(x, cooperators_changes_random[2], label="r = 5.0",linestyle = ':', color='dodgerblue')
#plt.plot(x, y[4],marker='o',markersize=8, linewidth=2.5, label="$r_a$ = 1.8", color='mediumblue')
#plt.plot(x, cooperators_changes_random[3], label="r = 5.1",linestyle = ':', color='mediumblue')
#plt.plot(x, y[5],marker='o',markersize=8, linewidth=2.5, label="$r_a$ = 2.4", color='mediumspringgreen')
#plt.plot(x, cooperators_changes_random[4], label="r = 5.2",linestyle = ':', color='mediumspringgreen')
#plt.plot(x, y[6],marker='o',markersize=8, linewidth=2.5, label="$r_a$ = 3.0", color='tan')




plt.legend(loc=(1,1),bbox_to_anchor=(0.7,0.2),frameon=False,fontsize=12,ncol=1)

plt.xlabel('p',fontsize=15)
plt.ylabel('$f_c$',fontsize=16,rotation=0,labelpad=10)
plt.tick_params(axis='both')
#plt.yticks(np.arange(0,1600,100))
plt.yticks(size=15)
#plt.xticks(np.arange(1,2.51,0.3),size=20)
plt.xticks(size=15)
plt.grid(True)
plt.show()

