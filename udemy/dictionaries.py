
# Declaração de um dicionario
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(my_dict['key1'])

print()

prices_lookup = {'apple': 1.99, 'oranges': 2.99, 'milk': 3.50}
print(prices_lookup)
print(prices_lookup['apple'])
print(prices_lookup['milk'])

print()

dic = {'k1': 12, 'k2': [4, 5, 6], 'k3': {'insideKey': 10}}
print(dic)
print(dic['k2'][1])
print(dic['k3']['insideKey'])

prices_lookup['apple'] = 4.0
prices_lookup['orange'] = 2.0
prices_lookup['soda'] = 1.99

print(prices_lookup.items())
print(dic.keys())
print(my_dict.values())



