# 1 - Função de potencia de um número
power = lambda num: num ** 2
print(power(5))

# 2 - Função que verificar se o número é par
par = lambda x:x % 2 == 0
print (par(27))

# 3 - Função que divide um numéro por outro
div_num = lambda x,y: x/ y
print(div_num(10,2))

# 4 - Função que investe uma string
reverse_string = lambda s:s[::-1]
print(reverse_string("Python"))

# 5 - Funcionalidade relacionada aos filmes
listaFilmes = ["Ela dança, Eu danço 3", "A cinco passos de você", 
             "Velozes e Furiosos 5", "Harry Potter e o Prisioneiro de Azkabam"]

nota = {
    "Ela dança, Eu danço 3": [10, 9.9, 9.5],
    "A cinco passos de você": [10, 9.8, 8.0],
    "Velozes e Furiosos 5": [10, 9.6, 8.7],
    "Harry Potter e o Prisioneiro de Azkabam": [10, 9.7, 7.5]
}

# Função para calcular a média de avaliações de um filme
media_nota = lambda nome_filme: sum(nota[nome_filme]) / len(nota[nome_filme])
print(f"Média de avaliação do filme: Ela dança, Eu danço 3: {media_nota("Ela dança, Eu danço 3")}")

# Função que verifica se um filme está na lista
check_movie = lambda nome_filme: nome_filme in listaFilmes
print(f"Velozes e Furiosos 5 está na lista? {check_movie("Velozes e Furiosos 5")}")

#Função para recomendar um filme com base na avaliação média
recomendo_filme = lambda nome_filme: f"Recomendo assistir {nome_filme} com média de {media_nota(nome_filme):.2f}"
print(f"{recomendo_filme("Harry Potter e o Prisioneiro de Azkabam")}")