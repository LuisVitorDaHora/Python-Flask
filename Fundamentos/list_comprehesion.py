# 1- Listando valores de 0 a 10 que seja menores do que 4

lista_numeros = [i for i in range(10) if i < 4]
print (lista_numeros)

print ("----------------------------------------------------")

# Lista de filmes
listFilms = ["Ela dança, Eu danço 3", "A cinco passos de você", 
             "Velozes e Furiosos 5", "Harry Potter e o Prisioneiro de Azkabam"]

# 2 - Filmes que possuem a letra "e" no titulo
FilmescomC = [filme for filme in listFilms if "c" in filme.lower()]
print(FilmescomC)

print ("----------------------------------------------------")

# 3 - Filmes que eu assistir 
FilmesVisto = [filme for filme in listFilms if filme != "Harry Potter e o Prisioneiro de Azkabam"]
print (FilmesVisto)

print ("----------------------------------------------------")

# 4 - Encontrando um filme pelo nome
while True:
    pesquisa_nome = input("Digite o nome do filme para buscar na lista (ou sair para encerrar): \n")
    if pesquisa_nome.lower() == "sair":
        print("Programa Encerrado")
        break

    foundfilmes = [filme for filme in listFilms if pesquisa_nome.lower() in filme.lower()]
    if foundfilmes:
        print(f"Filme(s) encontrado(s) com o nome: {pesquisa_nome}")
        for foundfilmes in foundfilmes:
            print(foundfilmes)
            print ("----------------------------------------------------")
    else:
        print(f"Nnenhum filme foi encontradi com o nome {pesquisa_nome}. Tente novamente!")