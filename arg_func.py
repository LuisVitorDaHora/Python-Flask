# Funçaõ para imprimir um nome completo

def nome_completo(pri_nome, seg_nome):
    print(f"Nome é: {pri_nome} {seg_nome}")

nome_completo("Luis Vitor", "Santos da Hora")

print ("----------------------------------------------------")

# 2 - Função para somar 2 numeros

def soma_numeros(a,b):
    return a + b

print(f"Soma é: {soma_numeros(10,50)}")

print ("----------------------------------------------------")

# 3 - Função com parâmetro default
def endereco(country = "Brasil"):
    print(f"Eu moro em: {country}")
    print ("----------------------------------------------------")

endereco()

# 4 - Função para avaliar filme
def rate_movie(num_ratings,nome_filme):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme: \n "))
        total += note
        
    if num_ratings > 0:
        media = total / num_ratings
    else:
        media = 0
    
    print(f"Média de avaliação do filme: {nome_filme} é {media:.2f}")

rate_movie(2,"Sonic")