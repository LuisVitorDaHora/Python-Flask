class Game:
    def __init__(self, name="", ano_lancamento=0, multiplayer=0, nota=0):
        self.name = name
        self.ano_lancamento = ano_lancamento
        self.multiplayer = multiplayer
        self.nota = nota
        self.totalEvaluation = 0  
        self.evaluators = 0   

    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("----- Dados do jogo -----")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.ano_lancamento}")
        print(f"Modo Multiplayer?: {self.multiplayer}")
        print(f"Avaliação do Jogo: {self.nota}\n")

class GameStudio:
    def __init__(self, name=""):
        self.name = name
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def evaluate_studio_quality(self):
        total_notes = sum(game.nota for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estudio {self.name} ainda não lançou jogo")
        else:
            average_note = total_notes / num_games
            print(f"Avaliação média dos jogos do estúdio {self.name}: {average_note:.2f}")

game1 = Game("Hogwarts Legacy", 2023, False, 9.2)
game2 = Game("God of War", 2018, False, 9.8)
game3 = Game("The Last of Us", 2013, False, 9.5)

studio = GameStudio("Naughty Dog")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()
for game in studio.games:
    game.technical_sheet()