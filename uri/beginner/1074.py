entrada = int(input())
numeros = []

for _ in range(0, entrada):
    numeros.append(int(input()))

for num in numeros:
    if num == 0:
        print("NULL")
    elif num % 2 == 0:
        if num > 0:
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    elif num % 2 != 0:
        if num > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")

