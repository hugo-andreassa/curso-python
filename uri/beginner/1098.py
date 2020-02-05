i = 0.0
j = 1.0

cont = 0

while i <= 2:
    print("I={:1.0} J={:1.1}".format(i, j))
    j += 1
    cont += 1

    if cont >= 3:
        j -= 1.2
        i += 0.2

        cont = 0



