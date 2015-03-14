from random import randint

sorteado = randint(1,100)

chute = 0

while sorteado != chute:
	chute = int(input("Chute: "))
	
	if chute == sorteado:
		print "Voce venceu!"
	else:
		if chute > sorteado:
			print "Alto"
		else:
			print "baixo"

print "FIm de jogo!"
