#cois, qtd = input().split(' ')
#cois, qtd = int(cois), int(qtd)

entradas = input().split(' ')
cois = int(entradas[0])
qtd = int(entradas[1])


calcas_s = input().split(' ')
calcas = []

for i in calcas_s:
    calcas.append(int(i))

cont = 0

for i in calcas:
    if i > cois:
        cont += 1

print(cont)