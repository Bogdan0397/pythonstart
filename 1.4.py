smallbotl = int(input("Input a number of bottles which volume is less then 1 litr: "))
largebotl = int(input("Input a number of bottles whic voluve is more then 1 litr: "))

smallbottl_price = smallbotl * 0.10
largebotl_price = largebotl * 0.25

sum = smallbottl_price + largebotl_price

print("You earned %.2f"%sum,"$")