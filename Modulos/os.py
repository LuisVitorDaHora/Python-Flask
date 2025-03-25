import os

# 1 Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versão do sistema operacional
os.system("ver")

# 4 - Configurações das Maquinas
os.system("systeminfo")

# 5 - Limpar a tela do Terminal
os.system("cls")

# 6 - Desligar o computador
os.system("shutdown /s")

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")

def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800")

def cancelar_desligamento():
    os.system("shutdown /a")
