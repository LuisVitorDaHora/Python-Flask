filmInception = {
    "tittle": "Inception",
    "ano": 2010,
    "imdb": 9.9,
    "gênero": ["Sci-fi", "Action", "Thriller"]
}
print(filmInception)
print(len(filmInception))
print (type(filmInception))

# 1 - Recuperar o elemento do dicionario
print(filmInception["gênero"])
print(filmInception.get("imdb"))

# 2 - Buscar apenas as chaves do dicionario
print(filmInception.keys())

# 3 - Buscar apenas os valores do dicionarios
print(filmInception.values())

# 4 - Buscar itens do dicionarios
print(filmInception.items())

# 5 - Adcionar itens no dicionario
filmInception["diretor"] = "Luis Vitor"
print(filmInception)

# 6 - Atualizar itens no dicionario
filmInception.update({"imdb": 8.7})
print(filmInception)

# 7 - Remover um item no dicionario
filmInception.pop("diretor")
print(filmInception)