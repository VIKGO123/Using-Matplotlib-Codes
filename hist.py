import matplotlib.pyplot as plt
ages=[5,2,3,4,5,10,12,14,89,99,45,66,44,55.22,11,33]
range=(0,100)
bins=10
plt.hist(ages,bins,range,rwidth=0.9,color='red',histtype='bar')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my first graph')

plt.show()
