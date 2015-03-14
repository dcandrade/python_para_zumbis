import random

nomes = ''' Ana Maria Julia Beatriz Sabrina Mirela Heidmilla Marcela Carla Jessica Luiza Ingrid Karol Jamille Fernanda'''.split() #''' Separa nomes em array

nomes.sort()

print(' '.join(nomes))
sorteado =  random.choice(nomes)
chute = ''
while chute != sorteado:
	chute = input('Chute: ')
	if chute == sorteado:
		print("Parabens!")
	elif chute > sorteado:
		print("Alto")
	else:
		print("Baixo")
