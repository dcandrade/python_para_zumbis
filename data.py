#Lê uma tada no formato dd/mm/aaa e imprime o mês por extenso
meses = "Janeiro Fevereiro Marco Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro".split()
data = input("Digite a data: ")
d,m,a = data.split("/")
print(d, 'de', meses[(int(m))-1], "de", a)

