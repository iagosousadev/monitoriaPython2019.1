nota = float(input())
nota_quebrada = nota - int(nota)
nota_inteira = nota - nota_quebrada

if nota_quebrada > 0.5:
    print("Nota: ", (nota_inteira+1))
else:
    print("Nota: ", nota_inteira)
