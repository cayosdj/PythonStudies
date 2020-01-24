#24/01/2020
#Slices
print("LISTA DOS CHEGADOS EM DANÇA!!\n")
players = ['charles', 'martinelli', 'michael douglas', 'florence and the machine', 'albino']
print("Os três primeiros da lista")
print(str(players[0:3]) + "\n")
print("Do segundo ao quarto")
print(str(players[1:4]) + "\n")
print("Omitindo apenas os dois primeiros")
print(str(players[2:]) + "\n")

#looping slices

print("Aqui estão os 3 primeiros da lista em ordem alfabética")
players.sort()
for player in players[:3]:
	print(player.title())

#copying lists
print("\nCOMIDAS FAVORITAS!!\n")
minhas_comidas = ['ovo frito', 'farofa', 'linguiça calabresa']
amigos_comidas = minhas_comidas[:]
minhas_comidas.append('batata frita')
minhas_comidas.append('pastel')
amigos_comidas.append('hambúrguer')
amigos_comidas.append('churrasco')

print("Minhas comidas favoritas são: \n" + str(minhas_comidas))
print("As comidas favoritas dos meus amigos são: \n" + str(amigos_comidas))