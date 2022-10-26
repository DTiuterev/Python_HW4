# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
print('Задайте последовательность чисел через пробел, я выведу список неповторяющихся элементов последовательности:\n')
sequence = [int(n) for n in input().split()]
for i in range(len(sequence)):
    for j in range(len(sequence)):
        if i != j and sequence[i] == sequence[j]:
            break
    else:
        print(sequence[i], end=' ')

