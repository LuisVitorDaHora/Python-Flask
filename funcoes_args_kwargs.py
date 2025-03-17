"""
*Args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função
    - Os argumentos são passados como uma tupla
**Kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento.
    - Os argumentos são passados como um dicionario
"""

# 1 - Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print (f"Soma é: {sum_total}")

sum(7,9)

# 2 - Apresentação de Cursos
def apresentacao (**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print ("Lista de Cursos: ")
apresentacao(nome="Python", categoria = "BackEnd", nivel = "Iniciante")
apresentacao(nome="Visão computacional com Python", categoria = "IA", nivel = "Avançado")
apresentacao(nome="Dashboards com dash", categoria = "Data Science", nivel = "Intermediario")