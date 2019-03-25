maxima = float(input())
minima = float(input())

if maxima < minima:
    aux = maxima
    maxima = minima
    minima = maxima
    #maxima, minima = minima, maxima
    
soma = maxima + minima

for i in range(3):
    nota = float(input())
    if nota > maxima:
        maxima = nota
    if nota < minima:
        minima = nota
    soma += nota

soma -= (minima+maxima)

media = soma / 3

print("%.2f" % media)