import matplotlib.pyplot as plt


y0 = [10, 10, 10, 10, 10, 4, 4, 1]
y1 = [10, 10, 10, 10, 10, 10, 10, 10]
y2 = [10, 10, 10, 10, 10, 10, 10, 10]
x = [2, 3, 4, 5, 6, 7, 8, 9]
plt.plot(x, y0, label="Standard solver")
plt.plot(x, y1, label="MaxSAT solver")
plt.plot(x, y2, label="MaxSAT solver upperbound")
plt.title('Carrousel')
plt.ylabel('Problems solved')
plt.xlabel('Number of agents')
plt.legend()
plt.show()
