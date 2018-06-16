import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]

y=[2,5,7,9,6,1,3,6,4,1]
plt.scatter(x,y,label="stars",color="green",marker='*',s=30)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my first graph')
plt.show()
