total_compra = float(input("Informe o total da compra: "))
valor_pago = float(input("Informe o valor pago: "))

troco = valor_pago - total_compra

if troco < 0:
    print("Valor Insuficiente, faltaram R$%.2f" % -troco)
else:
    cedulas100 = int(troco / 100)
    troco = troco - (cedulas100 * 100)
    print("Cedulas de R$100.00: %d." % cedulas100)

    cedulas50 = int(troco / 50)
    troco = troco - (cedulas50 * 50)
    print("Cedulas de R$50.00: %d." % cedulas50)

    cedulas20 = int(troco / 20)
    troco = troco - (cedulas20 * 20)
    print("Cedulas de R$20.00: %d." % cedulas20)

    cedulas10 = int(troco / 10)
    troco = troco - (cedulas10 * 10)
    print("Cedulas de R$10.00: %d." % cedulas10)

    cedulas5 = int(troco / 5)
    troco = troco - (cedulas5 * 5)
    print("Cedulas de R$5.00: %d." % cedulas5)

    cedulas2 = int(troco / 2)
    troco = troco - (cedulas2 * 2)
    print("Cedulas de R$2.00: %d." % cedulas2)

    moedas1 = int(troco)
    troco = troco - moedas1
    print("Moedas de R$1.00: %d." % moedas1)

    troco = troco * 100

    moedas50 = int(troco / 50)
    troco = troco - (moedas50 * 50)
    print("Moedas de R$0.50: %d." % moedas50)

    moedas25 = int(troco / 25)
    troco = troco - (moedas25 * 25)
    print("Moedas de R$0.25: %d." % moedas25)

    moedas10 = int(troco / 10)
    troco = troco - (moedas10 * 10)
    print("Moedas de R$0.10: %d." % moedas10)

    moedas5 = int(troco / 5)
    troco = troco - (moedas5 * 5)
    print("Moedas de R$0.05: %d." % moedas5)

    print("Moedas de R$0.01: %d." % troco)