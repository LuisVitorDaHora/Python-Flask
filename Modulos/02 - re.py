import re

texto = "Udemy - uma plataforma com muitos cursos online!"

# 1 - Indice de inicio e fim da palavra
# O r significa que é uma string raw(String bruta)
match = re.search(r"muitos cursos", texto)
print(f"Indice de inicio: {match.start()}")
print(f"Indice de fim: {match.end()}")

# Buscando o indice que possui o ponto
site = "https://udemy.com"
match = re.search(r"\.", site)
print(match)

# Buscar uma lista de caracteres dentro de uma frase
pattern = "[a-m]"
result = re.findall(pattern, texto)
print(result)

# 4 - Verificando o inicio de uma string
rule = r"^A"
phrases = ["A casa está suja", "O dia está lindo", "Vamos passear"]
for f in phrases:
    if re.match(rule, f):
        print(f"Encontrado: {f}")
    else:
        print(f"Não encontrado: {f}")

# 5 - Verificando o final de uma string
rule_end = r"!$"
phrases = "O dia está lindo!"
match = re.search(rule_end, phrases)
if match:
    print("Encontrado")
else:
    print("Não encontrado")
