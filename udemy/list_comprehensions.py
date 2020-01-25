
# Jeito Convencional
from typing import List, Union

mystring = "Hello"
mylist = []

for letter in mystring:
    mylist.append(letter)

# print(mylist)


# List Comprehensions
mylist = [letter for letter in mystring]
# print(mylist)

mylist = [x for x in "This girl's on fire"]
# print(mylist)

mylist = [num**2 for num in range(0, 11)]
# print(mylist)

mylist = [num for num in range(0, 11) if num % 2 == 0]
# print(mylist)

# if and else statement inside a list
mylist = [num if num % 2 == 0 else 'ODD'
          for num in range(0, 11)]
# print(mylist)

# Comparação do jeito convencional com a
# construção em lista
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
# print(fahrenheit)

for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))

# print(fahrenheit)

# Loops aninhados comparação
mylist = []

for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        mylist.append(x*y)

# print(mylist)

mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 100]]

# print(mylist)
