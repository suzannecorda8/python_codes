first = int(input("Enter first number:"))
operator = input("Enter the operator(+,-,/,*,%):")
second = int(input("Enter the second number:"))
if operator == "+ ":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid operation:")

