listFilms = ["Ela dança, Eu danço 3", "A cinco passos de você", 
             "Velozes e Furiosos 5", "Harry Potter e o Prisioneiro de Azkabam"]

# 1 - iterando valores de uma lista de filmes usando while
index = 0
while index < len(listFilms):
    print (listFilms[index])
    index += 1

print ("----------------------------------------------------")

# 2 - Quando a condição for atendida, o Loop será encerrado
index = 0
while index < len(listFilms):
    if listFilms[index] == "Velozes e Furiosos 5":
        break
    print (listFilms[index])
    index += 1

print ("----------------------------------------------------")

# 3 - Quando a condição for atendida, o Loop vai para proxima iteração
index = 0
while index < len(listFilms):
    if listFilms[index] == "Velozes e Furiosos 5":
        index += 1
        continue
    print (listFilms[index])
    index += 1

print ("----------------------------------------------------")

# 4 - Avaliação do filme com while
nome = input("Digite o nome do filme: \n")
nota = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
count = 0

while count < nota:
    note = float(input("Digite a nota para o filme: \n"))
    total += note
    count += 1

if nota > 0:
    media = total / nota
else:
    media = 0

print (f"Média de avaliação fo filme {nome} é {media:.2f}")
