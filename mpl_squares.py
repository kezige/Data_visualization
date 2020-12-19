import  matplotlib.pyplot as plt
input_values=[1,2,3,4,5]
squares = [1,4,9,16,25]
# plot()的默认第一个数据点的对应的x的坐标值为0，当做以下操作时，立刻改变此行为
plt.plot(input_values,squares,linewidth=2)

# 设置绘制线条的粗细
# plt.plot(squares,linewidth=1)
# 设置图标标题及字体大小
plt.title("Square Numbers",fontsize=24)
# 设置x轴和y轴的标签和字体大小
plt.xlabel("value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
# plt.plot(squares)

plt.show()