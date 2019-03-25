opc = input()
jog1_1 = int(input())
jog1_2 = int(input())
jog2_1 = int(input())
jog2_2 = int(input())

soma = jog1_1 + jog1_2 + jog2_1 + jog2_2

if (opc == 'p' and soma % 2 == 0) or (opc == "i" and soma % 2 != 0):
    print("venceu")
else:
    print("perdeu")