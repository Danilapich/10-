# Чтение данных из файла
with open('Пичугин_у234_vvod.txt', 'r') as file:
    lines = file.readlines()

# Преобразование данных в числа
matr = []
for line in lines:
    row = list(map(int, line.split()))
    matr.append(row)

# Вычисление результата
result = max([max(row) for row in matr if row == sorted(row) or row[::-1] == sorted(row)])

# Вывод результата в консоль
print(result)

# Запись результата в файл
with open('Пичугин_у234_vivod.txt', 'w') as file:
    file.write(str(result))