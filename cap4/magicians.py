#21/01/2020 - Cap 4
#Magicians Code List

magicians =['caelia', 'decadas','carl jung', 'helena blavatsky', 'aleister crowley', 'hermes trimegisto', 'liz greene','valdivia', 'saldino' , 'jaques de molay', 'gandalf', 'mago anael do youtube'];
magicians.sort()
print("Lista dos Magos: ") 
for magician in magicians:
	print(magician.title() + ", that was a great trick")
	print("I can't wait for see your next trick, " + magician.title() + ".\n")

print("'For every magician in the list of magicians, print the magician’s name.'")

#27/01/2020
#Slices 4-10

print("\nOs primeiros nomes da lista são: " + str(magicians[0:3]))
print("\nNomes do meio da lista: " + str(magicians[3:6]))
print("\nUltimos 3 nomes da lista: " + str(magicians[-3:]))