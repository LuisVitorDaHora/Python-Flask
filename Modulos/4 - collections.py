from collections import Counter, namedtuple, deque
from operator import itemgetter

# Lista de frutas (contagem)
frutas = ['banana', 'laranja', 'banana', 'Maçã', "Uva", "Uva", "Maçã"]
print(frutas)
print(Counter(frutas))

print('-------------------')

# Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price','note'])
g1 = game ('God of War', 50, 9.5)
g2 = game ('NBA2K25', 60, 8.5)
print(g1)
print(g2)

print('-------------------')

# Ordernando dicionários

estudantes = {'João': 8, 'Maria': 9, 'Pedro': 7, 'Ana': 10}
a = sorted(estudantes.items(), key=itemgetter(0))
print(a)

print('-------------------')

# Utilizando uma fila em ambas extremidades
fila = deque([20, 30, 40, 50])
fila.appendleft(10)
print(fila)
fila.append(60)
fila.popleft()
fila.pop()
print(fila)