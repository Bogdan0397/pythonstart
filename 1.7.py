things = int(input("Введите количество безделушек: "))
souvenirs = int(input("Введите количество сувениров: "))

things_weight = things * 0.112
souv_weight = souvenirs * 0.075

weight = things_weight + souv_weight

print("Вес посылки: ", weight , "kg")