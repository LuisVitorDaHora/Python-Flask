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

game1 = Game("Hogwarts Legacy", 2023, False, 9.2)
game2 = Game("God of War", 2018, False, 9.8)
game3 = Game("The Last of Us", 2013, False, 9.5)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9.5)
game1.evaluate(8.5)
game1.average()


# Exibindo o total de jogos criados
print(f"Total de jogos criados: {Game.Total_Games}")