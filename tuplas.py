filmsTuple = ("Inception", "The Shawshank Redemption", 
             "The Dark Kgnith", "Pulp Fiction", "Interstellar")
print(type(filmsTuple))

# 1 - Biscar os dois primeiros itens da tupla
print(filmsTuple[:2])

# 2 - Buscar o ultimo filme
print(filmsTuple[-1])

# 3 - Buscar filmes até uma determinada posição
print(filmsTuple[:3])

# 4 - Buscar filmes de uma posição em diante
print(filmsTuple[2:])

# 5 - Recuperar um item da tupla pelo nome
print(filmsTuple.index("Pulp Fiction"))