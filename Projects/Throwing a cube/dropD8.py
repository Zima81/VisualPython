from matplotlib import pyplot as plt
from dieClass import Die


#num_sides = int(input('Количество граней у кубика?: '))
die1 = Die(8)
die2 = Die(8)
# Моделирование бросков кубика, с сохранением в список
#roll_num = int(input('Сколько раз бросить кубик: '))
results = []
for _ in range(1000):
    results.append(die1.roll() + die2.roll())

# Подсчет частоты выпадания
max_result = die1.numsides + die2.numsides
frequency = []
for value in range(2, max_result+1):
    el = results.count(value)
    frequency.append(el)

fig, ax = plt.subplots()
ax.bar(range(2, max_result+1), frequency)

plt.show()


#plt.show()


