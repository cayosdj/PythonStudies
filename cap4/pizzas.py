#22/01/2020
#4-1 Pizzas:

pizzas = ['frango com catupiry', 'milho com mussarela', 'napolitana', 'portuguesa', 'a moda da casa', 'calabresa', 'bacon']

for pizza in pizzas:
	print("Eu gosto da pizza sabor: " + pizza.title())
print("Eu amo pizza, MAMA MIA!!")

#27/01/2020
#4-11 My Pizzas, Your Pizzas
print("\n")

friend_pizzas = pizzas[:]

pizzas.append('atum')
friend_pizzas.append('vegetariana')

for pizza in pizzas:
	print("Meus sabores favoritos de pizza são:" + str(pizza))

print("\n")

for friend_pizza in friend_pizzas:
	print("Os sabores favoridos de pizza do meu amigo são:" + str(friend_pizza))
