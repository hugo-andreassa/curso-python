
ddd_estado = {'61': 'Brasilia',
              '71': 'Salvador',
              '11': 'Sao Paulo',
              '21': 'Rio de Janeiro',
              '32': 'Juiz de Fora',
              '19': 'Campinas',
              '27': 'Vitoria',
              '31': 'Belo Horizonte'}

ddd = int(input())
estado = ddd_estado.get(str(ddd))

if estado is None:
    print('DDD nao cadastrado')
else :
    print(estado)
