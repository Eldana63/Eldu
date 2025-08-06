# Simple one-time calculator – works for one calculation only


num1 = float(input("Enter the first number: "))
op = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(f"{num1} {op} {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} {op} {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} {op} {num2} = {num1 * num2}")
elif op == "/":
    if num2 != 0:
        print(f"{num1} ÷ {num2} = {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator entered.")


       