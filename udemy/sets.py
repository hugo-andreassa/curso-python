# Declaração de um conjunto(set)
my_set = set()
my_set.add(1)
my_set.add(1)
my_set.add(2)

# O 1 só aparece uma vez, conjuntos só aceitam valores únicos, nunca se repetindo
print(my_set)

my_list = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]

# Transforma a lista em um conjunto com valores únicos
print(set(my_list))
print(set('Mississipi'))
