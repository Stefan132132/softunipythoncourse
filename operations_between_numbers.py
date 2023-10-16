num1 = int(input())
num2 = int(input())
math_operator = input()

if math_operator == "+":
    sum = num1 + num2
    if sum % 2 == 0:
        print(f"{num1} + {num2} = {sum} - even")
    else:
        print(f"{num1} + {num2} = {sum} - odd")
elif math_operator == "-":
    sum = num1 - num2
    if sum % 2 == 0:
        print(f"{num1} - {num2} = {sum} - even")
    else:
        print(f"{num1} - {num2} = {sum} - odd")
elif math_operator == "*":
    sum = num1 * num2
    if sum % 2 == 0:
        print(f"{num1} * {num2} = {sum} - even")
    else:
        print(f"{num1} * {num2} = {sum} - odd")
elif math_operator == "/":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        sum = num1 / num2
        print(f"{num1} / {num2} = {sum}")
elif math_operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        sum = num1 % num2
        print(f"{num1} % {num2} = {sum}")