import matplotlib.pyplot as plt

deg = [0, 1, 8, 27, 64]  # manual
x_line = list(range(5001))
y_line = [i**3 for i in x_line]

fig, ax = plt.subplots()
# ax.plot(deg)
ax.scatter(x_line, y_line, c=y_line, cmap=plt.cm.Reds, s=10)

plt.show()
