num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

if num1 >= num2:
    if num1 >= num3:
        max_num = num1
    else:
        max_num = num3
else:
    if num2 >= num3:
        max_num = num2
    else:
        max_num = num3

if num1 <= num2:
    if num1 <= num3:
        min_num = num1
    else:
        min_num = num3
else:
    if num2 <= num3:
        min_num = num2
    else:
        min_num = num3

print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
