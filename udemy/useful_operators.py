
mylist = [1, 2, 3]

# range() = [start, stop [, step]]
for num in range(1, 10, 2):
    pass
#   print(num)

# generator
list(range(0, 11, 2))
# print(list(range(0, 11, 2)))

word = "abcde"

# Função enumerate retorna tuplas contendo o index
# e o valor do index da 'lista' passada.
# Essa tupla pode ser acessada usando a mesma função
# de unpacking
for index, letter in enumerate(word):
    pass
#   print(f"{index}: {letter}")

# Função zip retorna uma tupla contendo as listas
# que foram passadas para serem 'zipadas' juntas
mylist1 = [1, 2, 3, 4, 5, 6]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

# O zip formara tuplas do tamanho da lista
# mais curta, ou seja se existir 3 listas,
# duas com 10 e uma com 3, ele formara 3
# tuplas
for item in zip(mylist1, mylist2, mylist3):
    pass
#   print(item)

# Operaror IN: verifica se está dentro da
# lista e retorna um boolean
#
# False
'x' in [1, 2, 3]
# True
1 in [1, 2, 3]

# print('x' in [1, 2, 3])
# print(1 in [1, 2, 3])


