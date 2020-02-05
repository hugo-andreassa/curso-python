entrada = int(input())

valores = []


for _ in range(0, entrada):
    x, y = input().split()

    if int(x) > int(y):
        aux = x
        x = int(y)
        y = int(aux)
    else:
        x = int(x)
        y = int(y)

    total = 0
    for num in range(int(x)+1, int(y)):
        if num % 2 != 0:
            #print(num)
            total += num

    valores.append(total)

for num in valores:
    print(num)
