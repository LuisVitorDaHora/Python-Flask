import pprint

filmDict = {
    "inception": {
        "ano": 2010,
        "imdb": 9.9,
        "gênero": ["Sci-fi", "Action", "Thriller"]
    },
    "Interstellar": {
        "ano": 2014,
        "imdb": 9.9,
        "gênero": ["Sci-fi", "Drama"]
    },
    "The Dark Knight": {
        "ano": 2008,
        "imdb": 9.0,
        "gênero": ["Action", "Drama", "Crime"]
    }
}
pp = pprint.PrettyPrinter (depth=4)
pp.pprint(filmDict)

# 1 - Buscar uma informação dentro do dicionario aninhado
print(filmDict["Interstellar"]["gênero"])

# 2 - Adicionar novo item
filmDict ["inception"]["diretor"] = "Luis Vitor"
print(filmDict["inception"])

# 3 - Excluir um dicionario
del filmDict["The Dark Knight"]
pp.pprint(filmDict)