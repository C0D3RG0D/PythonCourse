n = int(input("Введите n (8, 16, 32, 64): "))

#При этих значениях треугольник выводится полностью
if n <= 8:
    n = 8
elif n <= 16:
    n = 16
elif n <= 32:
    n = 32
else:
    n = 64

for row in range(n):
    for column in range(row + 1):

        if column > row - column:
            column = row - column

        result = 1

        for i in range(column):
            result = (result * (row - i)) // (i + 1)

        if result % 2 == 0:
            print(' ', end=" ")
        else:
            print('*', end=" ")

    print()
