filmsList = ["Inception", "The Shawshank Redemption", 
             "The Dark Kgnith", "Pulp Fiction", "Interstellar"]

# 1 - Tamanho da lista
print(len(filmsList))

# 2- Recuperar um intem da lista pelo indice
print(filmsList.index("Interstellar"))

# 3 - Adicionar item ao final da lista
filmsList.append("Homem Aranha")
print(filmsList)

# 4- Ordenar a lista
filmsList.sort()
print(filmsList)

# 5- Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Pulp Fiction")
print (filmsCopy)

# 6 - Remover todos os itens da lista
filmsList.clear()
print(filmsList)