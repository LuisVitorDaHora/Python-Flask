import random

# Selecionar um valor aleatorio de uma lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(lista))

print('----------------------------')

# Gera um número aleatorio em um intervalo de valores
r1 = random.randint(1, 100)
print(r1)

print('----------------------------')

# Seleciona um caractere aleatorio de uma string
name = 'Python'
r2 = random.choice(name)
print(r2)

print('----------------------------')

# Seleciona mais de um valor aleatorio
# random.sample(sequencia, tamanho)
print(random.sample(lista, 3))
print(random.sample(name, 3))
s = "Olá, mundo!"
print(random.sample(s, 2))

print('----------------------------')

# Programa de sorteio
done = False

while not done:
    print("O que você deseja fazer?")
    print("1 - Sortear um número")
    print("2 - Sair")

    choice = input(">")
    if choice == '1':
        print("---Adivinhe o número sorteado de 1 a 10:---\n")
        number = int(input("Digite o número de 1 a 10:\n"))
        result = random.randint(1, 10)
        if number == result:
            print(f"Parabéns! Você acertou! O número sorteado foi {result}")
        else:
            print(f"Que pena! Você errou! O número sorteado foi {result}")
    elif choice == '2':
        done = True
    else:
        print("Opção inválida! Tente novamente.")
