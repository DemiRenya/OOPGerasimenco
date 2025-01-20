print("Введите последовательность чисел, оканчивающуюся на 0:")
sequence = []
while True:
    num = int(input())
    if num == 0:
        break
    sequence.append(num)


max_count = 0
current_count = 1

for i in range(1, len(sequence)):
    if sequence[i] == sequence[i - 1]:
        current_count += 1
    else:
        max_count = max(max_count, current_count)
        current_count = 1


max_count = max(max_count, current_count)

print("Элементы введенные пользователем:", sequence)
print("Наибольшее число подряд идущих одинаковых элементов:", max_count)
