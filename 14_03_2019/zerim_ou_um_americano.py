j1 = int(input())
j2 = int(input())
j3 = int(input())
j4 = int(input())

soma = j1 + j2 + j3 + j4

if soma == 0:
    print("nenhum")
elif (soma % 4) == 0:
    print("jog4")
elif (soma % 4) == 1:
    print("jog1")
elif (soma % 4) == 3:
    print("jog3")
elif (soma % 4) == 2:
    print("jog2")
