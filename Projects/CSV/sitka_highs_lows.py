import csv
from datetime import datetime
from matplotlib import pyplot as plt

file_name = 'sitka_weather_2014.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    """Просмотр колонок с индексами"""
    # for i in range(len(header_row)):
    #     print(i, header_row[i])

    # Чтение дат и максимальных температур из файла, индекс 2 row[2]
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[2])
        low = int(row[3])
        dates.append(current_date)
        # high = round((high-32) / 1.8)  # преобразование из F в С
        highs.append(high)  # список максимальных значений
        lows.append(low)  # список минимальных значений

# Нанесение данных на диаграмму
plt.style.use('seaborn-v0_8-notebook')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Формироваание диаграммы
plt.title("Daily high temperatures, 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatue (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


