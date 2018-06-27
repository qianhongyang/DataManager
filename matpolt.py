#coding=utf-8
import matplotlib.pyplot as plt

xlist=[1,2,43,54,56]
ylist=[2,3,4,5,6]
alist=list(range(1,1001))
blist=[x**2 for x in alist]
# plt.plot(slist,linewidth=5)
# plt.title("QuickTron Test",fontsize=24)
# plt.xlabel("value",fontsize=14)
# plt.ylabel("key",fontsize=14)
# plt.tick_params(axis= 'both',labelsize=14)
plt.scatter(alist,blist,s=40,c=blist,edgecolors='none',cmap=plt.cm.Blues)
# plt.show()
plt.savefig("matplot_demo1.png")