movieName = "Top Gun"

movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura muito consgrado na indústria
"""

print (movieName.upper())
print (movieName.lower())
print (movieName.capitalize())
print (movieName.title())
print (movieName.center(10,'-')) # Retorna a string centralizada com caractere de preenchimento
print (movieName.find("u")) # Retorna a posição de um determinado caractere
print (movieName.find ("o"))
print (movieName.replace("Top", "Matrix")) # Altera elemento por outro
print (movieDescription.split(','))