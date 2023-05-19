def calculate_salary(h, r):
    return round((h* r), 2)


hour = float(input('Enter hour: '))
rate = float(input('Enter rate: '))

pay = calculate_salary(hour, rate)

print(f'Your salary is ${pay}')
