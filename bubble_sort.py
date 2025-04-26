mas = [38, 27, -13, 43, 3, 9, 82, 27, -5, 10]

n = len(mas)

for j in range(n-1):
    for i in range(n - 1 - j):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]

print(mas)