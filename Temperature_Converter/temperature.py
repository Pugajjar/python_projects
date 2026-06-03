# python simple Temperature converter


unit = input('Enter the Unit (C/F) : ')
temperature = float(input('Enter the Temperature you want to convert :' ))


if unit == 'C':
    celcius = 5 / 9 * (temperature - 32)
    print(celcius)

elif unit == 'F':
    fahrenheit = temperature * 5 / 9 + 32
    print(fahrenheit)
