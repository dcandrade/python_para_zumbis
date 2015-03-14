#verifica se a palavra lida é palídromo, supondo que não tem acentos

palavra = input("Digite a palavra:").lower()
print("E palidrome" if palavra==palavra[::-1] else "Nao e palindrome")
