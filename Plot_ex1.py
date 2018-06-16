import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]
a=[7,8,9]
b=[6,1,7]
plt.plot(x,y,label="line 1")
plt.plot(a,b,label="line 2",linestyle="dashed",linewidth=3,marker='o',markerfacecolor='blue',markersize=5)#adding legend
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my first graph')
plt.legend()#calling legend
plt.show()
