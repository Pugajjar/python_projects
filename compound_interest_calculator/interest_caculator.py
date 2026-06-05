# lets make the compounrd intrest calcuator
#formula is A = P(1 + (r/n))^t
'''
A -> Amount
P -> Principle (user input)
r -> Rate of interest (user input)
t -> time of interest (user input )
'''

principle = 0
rate = 0
time = 0

while principle <=0 :
    principle = float(input("Principle in ₹: "))
    if principle <=0:
        print('Principle cannot be <= 0')
print(f'The Principle is: {principle}')

while rate <=0 :
    rate = float(input("Rate in %: "))
    if rate <=0:
        print('rate cannot be <= 0')
print(f'The rate is (in %): {rate}')

while time <=0 :
    time = float(input("Time in years: "))
    if time <=0:
        print('time cannot be <= 0')
print(f'The time is: {time}')

#formula is A = P(1 + (r/n))^t
#FORMULA
amount = principle * pow((1 + (rate/100)), time )


print(f'The total amount is : ₹{amount:.2f}')
