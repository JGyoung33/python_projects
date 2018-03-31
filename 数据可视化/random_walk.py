from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self,num_points =5000):
        self.num_points = num_points

        #所有随机数都始于（0，0）
        self.x_values =[0]
        self.y_values =[0]


    def fill_walk(self):
        """计算漫步过程包含的所有的点"""

        #不断漫步知道列表包含所有的长度
        while len(self.x_values)<self.num_points:
            self.x_direction = choice([-1,1])
            self.y_direction = choice([-1,1])
            self.x_step = choice([0,1,2,3,4])
            self.y_step =choice([0,1,2,3,4])
            self.x_value = self.x_direction *self.x_step
            self.y_value = self.y_direction *self.y_step
            #拒绝原地踏步
            if self.x_step ==0 and self.y_step==0:
                continue
            next_x = self.x_values[-1] + self.x_value
            next_y = self.y_values[-1] + self.y_value

            self.x_values.append(next_x)
            self.y_values.append(next_y)
