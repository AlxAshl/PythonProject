import math

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

a = int(input("Введите первое число: "))
operation = str(input("Введите операцию: "))

if operation in ("r", "s2", "s3"):
    b = None
else:
    b = int(input("Введите второе число: "))



def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/" and b != 0:
        return a / b
    elif operation == "/" and b == 0:
        return "Ошибка: деление на ноль"
    elif operation == "s2":
        return a ** 2
    elif operation == "s3":
        return a ** 3
    elif operation == "r":
        return  math.sqrt(a)
    elif operation == "%":
        return a * (b/100)
    else:
        return "invalid operation"

result = calculate(a, b, operation)
print("Результат:", result)