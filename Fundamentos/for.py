# Lista de filmes

listFilms = ["Ela dança, Eu danço 3", "A cinco passos de você", 
             "Velozes e Furiosos 5", "Harry Potter e o Prisioneiro de Azkabam"]

# 1 - Iterando valores de uma lista 
for filme in listFilms:
    print (filme)

print ("----------------------------------------------------")

# 2 - Quando a condição for atendida, o loop será encerrado
for filme in listFilms:
    if filme == "Velozes e Furiosos 5":
        break
    print (filme)

print ("----------------------------------------------------")

# 3 - Quando a condição for atendida, o Loop vai para proxima iteração
for filme in listFilms:
    if filme == "Velozes e Furiosos 5":
        continue
    print(filme)

print ("----------------------------------------------------")

# 4 - Avaliação do filme:
nome = input("Digite o nome do filme: \n")
nota = int(input("Digite quantas avaliações deseja fazer: \n"))
total = 0

for i in range(nota):
    notaFilme = float(input("Digite a nota para o filme: \n"))
    total += notaFilme

if nota > 0:
    media = total / nota
else:
    media = 0

print (f"Média de avaliação fo filme {nome} é {media:.2f}")