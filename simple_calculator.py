'''
This is my first simple calculator for my github project
'''

num1 = float(input("Enter your number here:"))
op = input("Enter your operator:")
num2 = float(input("Enter your second number:"))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid Operator")