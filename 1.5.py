check = float(input("Input summ of your check in restraunt: "))

taxes = check * 0.0875
tips = check * 0.18

sum = taxes+tips

print("The taxes from your order is: %.2f" %taxes)
print("The tips is: %.2f" %tips)
print("Summ of all your taxes and tips is: %.2f" %sum)
