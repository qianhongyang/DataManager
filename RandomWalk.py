#coding=utf-8
from random import  choice

class RandomWalk():
    '''一个随机生成漫步数据的类'''

    def __init__(self,num_points=5000):
        self.num_points = num_points

        self.x_list=[0]
        self.y_list=[0]

    def fill_walk(self):
        while len(self.x_list) < self.num_points:
            x_dir=choice([1,-1])
            x_die=choice([0,1,2,3,4])
            x_step=x_dir*x_die
            y_dir = choice([1, -1])
            y_die = choice([0, 1, 2, 3, 4])
            y_step = y_dir * y_die

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_list[-1] + x_step
            next_y = self.y_list[-1] + y_step

            self.x_list.append(next_x)
            self.y_list.append(next_y)
