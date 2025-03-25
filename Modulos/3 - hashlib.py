import hashlib  

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Verificar algoritmos de acordo com SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHA256
algotimo = hashlib.sha256()
print(algotimo.digest)
messagem = "Melhor forma de prever o futuro é criá-lo".encode()
algotimo.update(messagem)
print(algotimo.hexdigest())

# 4 - Utlizando o MD5
md5 = hashlib.md5()
md5.update(messagem)
print(md5.hexdigest())