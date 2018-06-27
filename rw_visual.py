#coding=utf-8
import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

while True:
    rw=RandomWalk()
    rw.fill_walk()
    # plt.scatter(rw.x_list,rw.y_list,s=15)
    # plt.show()

    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_list,rw.y_list,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    plt.show()

    keep_runing=input("Make another walk? y/n" )
    if keep_runing == 'n':
        break