# Classe Pai (Superclasse)
class Game:
    Total_Games = 0 # Contador de jogos
    def __init__(self, name="", ano_lancamento=0, multiplayer=0, nota=0):
        self.name = name
        self.ano_lancamento = ano_lancamento
        self.multiplayer = multiplayer
        self.nota = nota
        Game.Total_Games += 1
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

    def evaluate (self,nota):
        self.totalEvaluation += nota
        self.evaluators += 1
    
    def average(self):
        print(f"A média de avaliações do jogo {self.name} é: {self.totalEvaluation / self.evaluators}")

# Classe derivada (Subclasse) - Especializada 
class SinglePlayer(Game):
    def __init__(self, name="", ano_lancamento=0, nota = 0, storyline = ""):
        super().__init__(name, ano_lancamento, multiplayer=False, nota=nota)
        self.storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyline}\n")

multi_game = Game("Call of Duty", 2023, True, 9.5)
multi_game.technical_sheet()

sing_game =     SinglePlayer("The last of Us", 2013, 9.5, "Sobrevivência em um mundo pós-apocalíptico")
sing_game.technical_sheet()