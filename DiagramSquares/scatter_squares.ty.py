import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')  # стиль отображения
fig, ax = plt.subplots()

# ax.scatter(2, 4, s=200)  # s=200 размер точек
# ax.scatter(x_values, y_values, c='red' s=10)
# ax.scatter(x_values, y_values, c=(0, 0.8, 0) s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта, делений на осях
ax.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапозона для каждой оси
ax.axis([0, 1100, 0, 1100000])

plt.show()  # показать
#plt.savefig('squares_plot.png', bbox_inches='tight')  # сохранить, bbox_inches убирает пустое пространство
