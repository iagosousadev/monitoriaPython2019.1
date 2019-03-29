nota1 = float(input())

max = nota1
min = nota1
soma = nota1

for i in range(4):
    nota = float(input())

    if nota > max:
        max = nota
    if nota < min:
        min = nota
    soma += nota

media = (soma - min - max) / 3

print("%.2f" % media)
