deposit = float(input("Input your deposit in USD: "))

first_year = deposit * 0.04
second_year = (deposit+first_year) * 0.04
third_year = (deposit+second_year+first_year) *0.04

sum = deposit + first_year + second_year +third_year

print("First year summ: %.2f" %(deposit+first_year))

print("Second year summ: %.2f" %(deposit+first_year+second_year))

print("Third year summ: %.2f" %(deposit+first_year+second_year+third_year))
