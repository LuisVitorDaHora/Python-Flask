import statistics  

# Aplicando a media
print(statistics.mean([1, 2, 3, 4, 4]))

# Aplicando a mediana
print(statistics.median([1, 3, 4, 5, 7]))

# Aplicando a moda
print(statistics.mode([1, 2, 3, 3, 3, 4, 5]))

# Desvio padrão
"""
- Quanto mais proximo de 0 for o desvio padrão, significa que os
dados do conjunto estão mais dispersos.

"""
print(statistics.stdev([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))