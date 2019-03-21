A = int(input())
B = int(input())

soma = 0
i = A

while i <= B:
    if i % 2 == 0:
        soma += i
    i += 1
    
print(soma)