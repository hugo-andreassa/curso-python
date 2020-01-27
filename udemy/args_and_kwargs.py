
# *args - arguments
# **kwargs - keyword arguments


def my_func(a, b):
    # Returns 5% of the sum of a and b

    # A função sum() recebe uma tupla
    # como parâmetro
    return sum((a, b)) * 0.05


# print(my_func(40, 60))


# Nesse caso o argumento recebera
# tudo que for passado, armazenando
# em uma tupla
def my_func(*args):
    # print(args)
    return sum(args) * 0.05


# print(my_func(10, 20, 30, 40, 100))


# Nesse caso o argumento ira tratar
# tudo que for recebido como um
# dicionario
def my_func(**kwargs):
    print(kwargs)
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")


# my_func(fruit="banana", car="honda")


# *args and **kwargs
def my_func(*args, **kwargs):
    print("I would like {} {}".format(args[0], kwargs["food"]))


my_func(10, 2, 3, food='eggs')


