import matplotlib.pyplot as plt

x =[1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(x,squares, linewidth =5)
plt.title("Random Number", fontsize=30)
plt.xlabel("Value",fontsize = 20)
plt.ylabel("Value of square", fontsize =20)
#设置刻度标记
plt.tick_params(axis="both",labelsize =10)
plt.show()