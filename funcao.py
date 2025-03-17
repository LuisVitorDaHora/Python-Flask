# 1 - Função para imprimir uma mensagem
def bem_vindo():
    print ("----------------------------------------------------")
    print("Bem - Vindo ao sistema de filmes! ")
    print ("----------------------------------------------------")

bem_vindo()

# 2- Função para calcular a media de notas
def calcular_media():
    numero_avali = int(input("Digite quantas avaliações deseja fazer para o filme: \n "))
    print ("----------------------------------------------------")
    total = 0
    for i in range(numero_avali):
        note = float(input("Digite a nota para o filme: \n"))
        print ("----------------------------------------------------")
        total += note
    
    if numero_avali > 0:
        media = total / numero_avali
    else:
        media = 0
    
    return media

print(f"A média de avaliações é:  {calcular_media():.2f}")
print ("----------------------------------------------------")


# 3 - Função para cadastrar um filme: 

def criacao_filme():
    nome = input("Digite o nome do filme: \n")
    print ("----------------------------------------------------")
    ano = int(input("Digite o ano de lançamento do filme: \n "))
    print ("----------------------------------------------------")
    preco_filme = float(input("Digite o preço do filme: \n "))
    print ("----------------------------------------------------")
    nota = float(input("Digite a nota do filme: \n "))
    print ("----------------------------------------------------")
    print(f"{nome} ({ano}) - R$ {preco_filme:.2f}")

criacao_filme()