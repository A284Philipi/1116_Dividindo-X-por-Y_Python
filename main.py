casos = int(input())
cont = int(0)
while (cont < casos):
    a, b = input().split(" ")
    a = int(a)
    b = int(b)
    if (b == 0):
        print("divisao impossivel")
    else:
        media = float(a / b)
        print(media)
    cont = cont + 1