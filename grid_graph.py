import matplotlib.pyplot as plt


y0 = [10, 10, 10, 10, 10, 10, 10, 5]
y1 = [10, 10, 10, 10, 9, 10, 8, 2]
y2 = [10, 10, 10, 10, 7, 7, 3, 1]
x = [2, 3, 4, 5, 6, 7, 8, 9]
plt.plot(x, y0, label="Standard solver")
plt.plot(x, y1, label="MaxSAt solver")
plt.plot(x, y2, label="MaxSAT solver upperbound")
plt.title('Grid')
plt.ylabel('Y')
plt.xlabel('X')
plt.legend()
plt.show()
