primeiro = int(input())
segundohora = int(input())
segundominuto = int(input())
segundoseg = int(input())

segundo = (segundohora*3600) + (segundominuto*60) + segundoseg

if primeiro == segundo:
    print("empate")
elif primeiro < segundo:
    print("primeiro")
else:
    print("segundo")