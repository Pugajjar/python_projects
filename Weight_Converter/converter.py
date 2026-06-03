# python simple weight converter
# logic 1kg = 2.20462

# so we will take the KG from the user and multiply it by the pound
# pound = kg * 2.20462


choice = input('Enter the conversion you want to convert (KG or Pound):')

if choice == 'KG' or choice == 'kg':
    kg = float(input('Enter the Weight in kg:'))
    pound = kg * 2.20462
    print(f'The Weight in the pound is {pound} lbs')
elif choice == 'Pound':
    pound = float(input('Enter the Weight in pound:'))
    kg = pound / 2.20462
    print(f'The Weight in the pound is {kg} lbs')

else :
    print('Enter the valid argument !!!')
