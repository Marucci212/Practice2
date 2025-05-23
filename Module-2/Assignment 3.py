
# Display the Initial investment amount
# Display a given interest rate
# Display number of years to take the investment to double
def time_to_double(investment, interest_rate):
    years = 0
    target = investment * 2
    while investment < target:
        investment *= (1 + interest_rate / 100)
        years += 1
    return years
initial_investment = float(input('Enter investment amount: '))
interest_rate = float(input('Enter the interest rate: '))
years_needed = time_to_double(initial_investment, interest_rate)
print(f'It will take {years_needed} years for the investment to double.')