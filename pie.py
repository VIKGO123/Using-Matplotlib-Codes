import matplotlib.pyplot as plt
activities=['eat','sleep','work','play']
slices=[3,7,8,6]
colors=['r','m','g','b']
plt.pie(slices,labels=activities,colors=colors,startangle=90,shadow=True,explode=(0.1,0,0,0),autopct='%1.11f%%')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my first graph')
plt.show()
