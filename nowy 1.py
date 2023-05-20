hour = float(input('Enter your hour: '))
rate = float(input('Enter your rate per hour: '))
tax = (hour * rate) * (22 / 100)
pay = (hour * rate) - tax

print(f'Your salary per week is: {round(pay, 2)}zł')
