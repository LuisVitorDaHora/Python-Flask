class Game:
    def __init__(self, name="", ano_lancamento=0, multiplayer=0, nota=0):
        self.name = name
        self.ano_lancamento = ano_lancamento
        self.multiplayer = multiplayer
        self.nota = nota

    def __str__(self):
        return f"Game: {self.name}"

game1 = Game("Hogwarts Legacy", 2023, False, 9.2)
game2 = Game("God of War", 2018, False, 9.8)
game3 = Game("The Last of Us", 2013, False, 9.5)

print("----- Dados do jogo -----")
print(f"Nome do jogo: {game1.name}\nAno de lançamento: {game1.ano_lancamento}")
