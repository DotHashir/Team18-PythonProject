a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

operation = input("""Enter the operation you want to perform on the numbers
                  '+' for addition
                  '-' for subtraction
                  '*' for multiplication
                  '/' for division""")

if operation == '+':
    print("The result of", a, "+", b,"is", a+b)

elif operation == '-':
    print("The result of", a, "-", b,"is", a-b)

elif operation == '*':
    print("The result of", a, "*", b,"is", a*b)

elif operation == '/':
    if b == 0:
        print("Can not divide a number by 0")

    else:
        print("The result of", a, "/", b,"is", a/b)


else:
    print("The operation you input is not correct")