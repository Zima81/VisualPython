# Модель путь пыльцевого зерна на поверхности водяной капли
import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Новые блуждания строятся до тех пор, пока программа оставется активной
while True:
    # Построение случайного блуждания
    rw = RandomWalk()
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(16, 9), dpi=128)  # 1366 х 768 (16:9) 26"
    ax.plot(rw.x_values, rw.y_values, c='grey', linewidth=1)

    # Выделение перой и последней точек.
    ax.scatter(rw.x_values[0], rw.y_values[0], c='green', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    # Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
