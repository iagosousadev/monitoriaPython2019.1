salario = float(input())

if salario > 2000:
    salario *= 1.05
elif salario > 1500:
    salario *= 1.10
elif salario > 1000:
    salario *= 1.15
else:
    salario *= 1.20

print("%.2f" % novo_salario)

