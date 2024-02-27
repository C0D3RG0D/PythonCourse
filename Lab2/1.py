n = int(input("Введите n строк треугольника Паскаля: "))

for row in range(n):
    for column in range(row + 1):

        if column > row - column:
            column = row - column

        result = 1

        for i in range(column):
            result = (result * (row - i)) // (i + 1)

        print(result, end=" ")

    print()
