# 立方：数字的三次方被称为其立方。请绘制一个图形，显示前 5个整数的立方值，
# 再绘制一个图形，显示前 5000个整数的立方值。
# 彩色立方：给你前面绘制的立方图指定颜色映射
import matplotlib.pyplot as plt
# x_values=[1,2,3,4,5]
# y_values=[1,8,27,64,125]
x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]

plt.scatter(x_values,y_values,s=1,c=x_values,cmap=plt.cm.Reds,edgecolor='none')

plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis=([0,10,0,5000])
plt.show()