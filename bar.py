import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,24,36,40,5]
tick_label=['one','two','three','four','five']
plt.bar(x,y,tick_label=tick_label,width=0.9,color=['red','blue'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my first graph')

plt.show()
