import matplotlib.pyplot as plt
import numpy as np

c_heat=[[2.213308256,2.222451583,2.229,2.983163703,2.999465121,2.980530685,4.514105619,4.482379377,4.499605272,7.463243681,7.47207737,7.477882135],
[2.187845989,2.213,2.1784,2.986352155,2.9836,2.97366,4.472906841,4.48234,4.466461782,7.483673914,7.47211,7.4595],
[2.161689929,2.099,1.98,2.978026894,2.98178,2.95188,4.461207679,4.49,4.475,7.456050091,7.47487,7.4882],
[1.778312283,1.6854,1.01562288,2.940207265,2.92585,2.627,4.489810166,4.4727,4.347,7.458154819,7.487,7.48103289],
[1.776675103,1.0514,0.7958,2.936466455,2.6075,1.277169085,4.482813467,4.436,3.945895,7.481180271,7.467,7.400813732],
[1.187270896,0.8425,0.7574,2.866723844,1.17775344,1.036,4.477097213,4.113299159,3.1092786,7.491851541,7.454971744,7.2644],
[1.039386816,0.77344,0.7439,2.584750724,1.05,1.015,4.361750878,3.6346,1.6785,7.496020281,7.3086,6.8736],
[0.873066907,0.7597,0.754,2.075847779,1.0134,1.012,4.1401214,1.9395,1.5455,7.46106264,7.2269,6.4144],
[0.79,0.74687,0.7496,1.2173,1.025,1.0064,3.98,1.6115,1.5388,7.442435146,6.8343,5.7876],
[0.8213,0.7622,0.7535,1.0282,1.0075,1.0186,3.496,1.547,1.53,7.316,6.5137,5.047],
[0.769,0.750001645,0.756,1.041,1.016461699,1.02,3.4877,1.521699552,1.524,7.22586,6.13620914,4.676]]



x = [ 0.1*i for i in range(len(c_heat))]
y=[]

for i in range(0,len(c_heat[0])):
    y0=[]
    for j in range(len(c_heat)):
        y0.append(c_heat[j][i])
    y.append(y0)



plt.figure(figsize=(10, 8))

plt.figure(dpi=600)
plt.plot(x, y[0], marker='o', markersize=8, linewidth=2.5, label="HL b=1.0", color='green', linestyle='-') 
plt.plot(x, y[1], marker='o', markersize=8, linewidth=2.5, label="HL b=1.5", color='green', linestyle='-.') 
plt.plot(x, y[2], marker='o', markersize=8, linewidth=2.5, label="HL b=2.0", color='green', linestyle=':')  


plt.plot(x, y[3],marker='o',markersize=8, linewidth=2.5, label="SL b=1.0", color='orange', linestyle='-')
plt.plot(x, y[4],marker='o',markersize=8, linewidth=2.5, label="SL b=1.5", color='orange', linestyle='-.')
plt.plot(x, y[5],marker='o',markersize=8, linewidth=2.5, label="SL b=2.0", color='orange', linestyle=':')


plt.plot(x, y[6],marker='o',markersize=8, linewidth=2.5, label="XL b=1.0", color='dodgerblue', linestyle='-')
plt.plot(x, y[7],marker='o',markersize=8, linewidth=2.5, label="XL b=1.5", color='dodgerblue', linestyle='-.')
plt.plot(x, y[8],marker='o',markersize=8, linewidth=2.5, label="XL b=2.0", color='dodgerblue', linestyle=':')


plt.plot(x, y[9],marker='o',markersize=8, linewidth=2.5, label="WS b=1.0", color='red', linestyle='-')
plt.plot(x, y[10],marker='o',markersize=8, linewidth=2.5, label="WS b=1.5", color='red', linestyle='-.')
plt.plot(x, y[11],marker='o',markersize=8, linewidth=2.5, label="WS b=2.0", color='red', linestyle=':')


#plt.plot(x, cooperators_changes_random[2], label="r = 5.0",linestyle = ':', color='dodgerblue')  
#plt.plot(x, y[4],marker='o',markersize=8, linewidth=2.5, label="$r_a$ = 1.8", color='mediumblue')
#plt.plot(x, cooperators_changes_random[3], label="r = 5.1",linestyle = ':', color='mediumblue')
#plt.plot(x, y[5],marker='o',markersize=8, linewidth=2.5, label="$r_a$ = 2.4", color='mediumspringgreen')
#plt.plot(x, cooperators_changes_random[4], label="r = 5.2",linestyle = ':', color='mediumspringgreen')
#plt.plot(x, y[6],marker='o',markersize=8, linewidth=2.5, label="$r_a$ = 3.0", color='tan')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), frameon=False, fontsize=12, ncol=1)


# plt.legend(loc=(1,1),bbox_to_anchor=(0.7,0.2),frameon=False,fontsize=12,ncol=1)

plt.xlabel('m',fontsize=15)
plt.ylabel(r'$\bar{A}$',fontsize=13,rotation=0,labelpad=10)
plt.tick_params(axis='both')
#plt.yticks(np.arange(0,1600,100))
plt.yticks(size=15)
#plt.xticks(np.arange(1,2.51,0.3),size=20)


plt.xticks(size=15)
plt.grid(True)
plt.show()

