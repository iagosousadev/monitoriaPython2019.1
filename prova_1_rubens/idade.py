idade = int(input())

anos = int(idade / 365)
idade %= 365
meses = int(idade / 30)
idade %= 30
semanas = int(idade / 7)
idade %= 7

print("%d : %d : %d : %d" % (anos, meses, semanas, idade)) 
