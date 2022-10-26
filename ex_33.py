# 33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
k = int(input('Введите натуральную степень k:\n'))

import random

def random_coeff():
    return random.randint(0, 100)

def create_pn(k):
    list = [random_coeff() for i in range(k + 1)]
    return list

def create_str(sp):
    list = sp[::-1]
    wr = ''
    if len(list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(list)):
            if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
                wr += f'{list[i]}x^{len(list) - i - 1}'
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 2 and list[i] != 0:
                wr += f'{list[i]}x'
                if list[i + 1] != 0:
                    wr += ' + '
            elif i == len(list) - 1 and list[i] != 0:
                wr += f'{list[i]} = 0'
            elif i == len(list) - 1 and list[i] == 0:
                wr += ' = 0'
    return wr

def write_file(str):
    with open('polynomial_33.txt', 'w') as data:
        data.write(str)

coeff = create_pn(k)
write_file(create_str(coeff))

with open('polynomial_33.txt', 'r') as file_1:
    for line in file_1:
        print(f'В файл polynomia_33.txt записано множество {k}й степени со случайными коэффициентами:\n{line}')

