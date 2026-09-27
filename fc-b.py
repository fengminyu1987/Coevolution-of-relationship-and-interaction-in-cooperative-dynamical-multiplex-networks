import matplotlib.pyplot as plt
import numpy as np

c_heat=[[0.523752,	0.932116,	0.99794,	1],
[0.341796,	0.857522,	0.998,	1],
[0.17184,	0.847504,	0.866850909,	1],
[0.09656,	0.786816,	0.836485455,	1],
[0.09578,	0.424418,	0.8011618,	1],
[0.03838,	0.3335636,	0.765494545,	1],
[0.03856,	0.157333333,	0.739505455,	0.904465455],
[0.01308,	0.072804444,	0.699447273,	0.873403636],
[0.01692,	0.04588,	0.675307273,	0.851341818],
[0.01364,	0.0376666,	0.649534545,	0.815381818],
[0.0056,	0.0407733,	0.578973333,	0.783901818]]

x = [ 1+0.1*i for i in range(len(c_heat))]
y=[]

for i in range(0,len(c_heat[0])):
    y0=[]
    for j in range(len(c_heat)):
        y0.append(c_heat[j][i])
    y.append(y0)




plt.figure(dpi=600)
plt.plot(x, y[0],marker='o',markersize=8, linewidth=2.5, label="HL", color='green')
plt.plot(x, y[1],marker='o',markersize=8, linewidth=2.5, label="SL", color='orange')
plt.plot(x, y[2],marker='o',markersize=8, linewidth=2.5, label="XL", color='dodgerblue')
plt.plot(x, y[3],marker='o',markersize=8, linewidth=2.5, label="WS", color='red')



#plt.plot(x, cooperators_changes_random[2], label="r = 5.0",linestyle = ':', color='dodgerblue')
#plt.plot(x, y[4],marker='o',markersize=8, linewidth=2.5, label="$r_a$ = 1.8", color='mediumblue')
#plt.plot(x, cooperators_changes_random[3], label="r = 5.1",linestyle = ':', color='mediumblue')
#plt.plot(x, y[5],marker='o',markersize=8, linewidth=2.5, label="$r_a$ = 2.4", color='mediumspringgreen')
#plt.plot(x, cooperators_changes_random[4], label="r = 5.2",linestyle = ':', color='mediumspringgreen')
#plt.plot(x, y[6],marker='o',markersize=8, linewidth=2.5, label="$r_a$ = 3.0", color='tan')




plt.legend(loc=(1,1),bbox_to_anchor=(0.7,0.2),frameon=False,fontsize=12,ncol=1)

plt.xlabel('b',fontsize=15)
plt.ylabel('$f_c$',fontsize=16,rotation=0,labelpad=10)
plt.tick_params(axis='both')
#plt.yticks(np.arange(0,1600,100))
plt.yticks(size=15)
#plt.xticks(np.arange(1,2.51,0.3),size=20)
plt.xticks(size=15)
plt.grid(True)
plt.show()

