n = int(input())

soma = 0
cont = 0
for i in range(n):
    nota = int(input())
    if nota % 2 != 0 and nota > 5:
        soma += nota
        cont += 1

media = soma / cont

print("%d" % media)
