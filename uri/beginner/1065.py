
entrada = [int(input()), int(input()), int(input()), int(input()), int(input())]

entrada = [num for num in entrada if num % 2 == 0]

print("{} valores pares".format(len(entrada)))
