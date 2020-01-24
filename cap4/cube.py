#23/01/2020
#4-8 Cubes ^3
cubelist = []
for cubo in range(1,11):
	cubao = cubo ** 3
	print(cubao)
	cubelist.append(cubao)
print("lista dos ^3:" + str(cubelist))

#4-9 Cube Comprehension
cubelist2 = [value **3 for value in range(1,11)]
print("lista comprehension:" + str(cubelist2))