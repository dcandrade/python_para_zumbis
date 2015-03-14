#Faça uma função que dada uma palavra pule uma letra e devolva uma palavra sem a letra na posição dada.
#Exemplo: come('Python', 3) retorna Pyton

def come(string, i):
	return string[:i]+string[i+1:]

print(come("Python", 3))
