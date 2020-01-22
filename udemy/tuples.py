# Declaração de uma tupla
# Tupla são imutaveis
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

print(type(my_tuple))
print(type(my_list))

# Conta quantas vezes o elemento aparece
print(my_tuple.count(1))
# Devolve o index do elemento
print(my_tuple.index(1))

# OK
my_list[0] = 'NEW'
print(my_list)

# Devolve um erro, tuplas são imutaveis
my_tuple[0] = 'NEW'
print(my_tuple)
