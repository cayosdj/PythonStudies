#23/01/2020
#square with range function
print("\nUtilizando a função 'range': ")
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)


print(str(squares) + " \n")


#square with comprehension list

square2 = [value **2 for value in range(1,11)]
print("\nLista alternativa comprehension:\n" + str(square2) + "\n")


#estatística simples com lista de números

print("Menor dígito da lista:")
print(str(min(squares)) + " \n")

print("Maior dígito da lista:")
print(str(max(squares)) + " \n")

print("Soma dos dígitos da lista:")
print(str(sum(squares)) + "\n")