import matplotlib.pyplot as plt 

x = [1, 2, 4, 5]
y = [2, 4, 6, 9]

x2 =[1, 4 ,5]
y2= [10, 15, 12]

plt.plot(x,y, label= ' x and y')
plt.plot(x2,y2, label =' x2 and y2')
plt.xlabel('X Axis')
plt.ylabel('Y Asis')
plt.title('X and Y Graph\nIn Python')
plt.legend()
plt.show()