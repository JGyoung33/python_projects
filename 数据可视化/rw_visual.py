import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    #绘制出所有的点
    rw.fill_walk()
    # 设置绘图窗口的大小
    plt.show()

    plt.figure(dpi=128,figsize=(10, 6))
    points_number = list(range(rw.num_points))
    plt.scatter(rw.x_values[0],rw.y_values[0],c="red",edgecolors="none",s = 100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c="green",edgecolors="none",s=100)
    plt.scatter(rw.x_values,rw.y_values,c = points_number,cmap = plt.cm.hot,edgecolors="none",s =1)
    plt.title("Random Walk", fontsize=24)


    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running =input("Do you want to continue?(y/n)?")

    if keep_running == "y":
        break
