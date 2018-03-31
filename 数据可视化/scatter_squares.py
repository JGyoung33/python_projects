import matplotlib.pyplot as plt

x_values = list(range(1,1001))

y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.prism,edgecolors='none',s=30) #cmap与c的值构成了颜色映射
plt.title("Random Number", fontsize=30)
plt.xlabel("Value",fontsize = 20)
plt.ylabel("Value of square", fontsize =20)
#设置刻度标记
plt.tick_params(axis="both",which="major",labelsize =10)
plt.axis([0,1100,0,1100000000])

plt.savefig('square_figure.png',bbox_ichches ="tight")
plt.show()

