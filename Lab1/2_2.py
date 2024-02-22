n = int(input("Введите число n: "))


for i in range(n, 0, -1):
    print(" " * (n - i) + "".join(str(j) for j in range(i, 0, -1)) + "".join(str(j) for j in range(2, i + 1)))
        

