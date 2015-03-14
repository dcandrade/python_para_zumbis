def esconde(msg):
	resp=''
	for char in msg:
		resp = resp + chr(ord(char) + 30000) #ord iz o valor do char. Chr dá o char equivalente
	return resp

def mostra(msg):
	resp =''
	for char in msg:
		resp = resp + chr(ord(char) - 30000)
	return resp


msg = input("Insira o texto a ser criptografado: ")

msgCriptografada = esconde(msg)

print("Mensagem criptografada: ", msgCriptografada)
print("Mensagem original: ", msg)
