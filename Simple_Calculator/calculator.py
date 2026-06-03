operation = input('Enter the operation(*,+,-,/): ')
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

if operation == '+':
    print(f'Addition : {num1+num2}')
elif operation == '-':
    print(f'Subtraction : {num1 - num2}')
elif operation == '*':
    print(f'Multiplication : {num1 * num2}')
elif operation == '+':
    print(f'Division : {num1 / num2}')
else:
    print('Enter the valid character !!')
