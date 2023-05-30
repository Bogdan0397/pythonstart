alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

phrase = input("Input phrase: ")
num = int(input("Input num: "))
list_phrase = list(phrase)
print(list_phrase)
res = []
upper = []

for i in list_phrase:
     res+= alpha[(alpha.index(i)+num)%len(alpha)]


print(res)

