# 1 - Fatorial de um número
def fatorial(num):
    if num == 1:
        return 1
    else:
        return(num * fatorial(num -1))
number = int(input("Digite o número para o fatorial: \n"))
print(f"O fatorial de {number} é {fatorial(number)}")

# 2 - soma total de um número
def total_soma(num):
    if num == 1:
        return 1
    else:
        return (num + total_soma(num - 1))

num = int(input("Digite o número para soma: \n"))
print(f"A soma total de {num} é {total_soma(num)}")