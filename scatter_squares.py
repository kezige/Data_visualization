import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]

# 用颜色映射，浅颜色表示小值，反之，则大。如下是利用y的值来设置颜色
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=10)
# edgecolor可以用来删除黑色轮廓;可以用c来定义点的颜色,如果用RGB颜色指定的话，取值在0-1之间
# plt.scatter(x_values,y_values,c='green',edgecolor='none',s=10)
# plt.scatter(x_values,y_values,c=(0.2,0.5,0.1),edgecolor='none',s=10)

# 设置散点的位置及大小
# plt.scatter(2,4,s=10)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
# 设置刻度标记的大小，axis表示轴
plt.tick_params(axis='both',which='major',labelsize=14)

# axis可以设置x轴和y轴的起始点和结束点
plt.axis([0,1100,0,1100000])

# plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')