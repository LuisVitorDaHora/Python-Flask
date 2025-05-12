import tkinter as tk
import ORM
from tkinter import messagebox

def adicionar_jogo():
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    genero = entry_genero.get()
    ORM.adicionar_jogo(nome, ano, nota, genero)
    messagebox.showinfo("Sucesso", "Jogo adicionado com sucesso!")

def atulizar_jogo():
    id_jogo = entry_id.get()
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    genero = entry_genero.get()
    ORM.atulizar_jogo(id_jogo, nome, ano, nota, genero)
    messagebox.showinfo("Sucesso", "Jogo atualizado com sucesso!")

def deletar_jogo():
    id_jogo = entry_id.get()
    ORM.deletar_jogo(id_jogo)
    messagebox.showinfo("Sucesso", "Jogo deletado com sucesso!")


# Interface Gráfica
root = tk.Tk()
root.title("Sistema de Jogos")

# Rótulos e campos de entrada
label_id = tk.Label(root, text="ID do Jogo:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(root, text="Nome do Jogo:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_ano = tk.Label(root, text="Ano de Lançamento:")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=10, pady=5)

label_genero = tk.Label(root, text="Gênero:")
label_genero.grid(row=4, column=0)
entry_genero = tk.Entry(root, width=50)
entry_genero.grid(row=4, column=1, padx=10, pady=5)

# Botões
button_adicionar = tk.Button(root, text="Adicionar Jogo", command=adicionar_jogo)
button_adicionar.grid(row=5, column=0, columnspan=2, pady=5)

button_atulizar = tk.Button(root, text="Atualizar Jogo", command=atulizar_jogo)
button_atulizar.grid(row=6, column=0, columnspan=2, pady=5)

button_deletar = tk.Button(root, text="Deletar Jogo", command=deletar_jogo)
button_deletar.grid(row=7, column=0, columnspan=2, pady=5)


root.mainloop()