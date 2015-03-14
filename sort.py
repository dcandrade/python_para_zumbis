from random import randint

sorteado = randint(1,100)

while True:
	chute = int(input("Chute: "))
	if chute == sorteado:
		print("Voce venceu!")
	else: 
		print('Alto' if chute > sorteado else 'Baixo')

print("Fim de jogo!")
