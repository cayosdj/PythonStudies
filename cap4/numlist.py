#23/01/2020
#4-3 Contando até vinte
print("\nContando até vinte:")
for vinte in range(1,21):
	print(vinte)

#4-4 Um Milhão
#mil porque um milhão travou meu PC :(
milhao = []
print("\nContando até mil hão")
for numeros in range(1,100001):
	milhao.append(numeros)
	#print(numeros)
print("lista do milhão")
print(milhao)

#4-5
#min max sum do milzao
print("Min, Max, Soma da lista: ")
print(min(milhao))
print(max(milhao))
print(sum(milhao))