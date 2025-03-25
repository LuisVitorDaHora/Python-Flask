import tkinter as tk

# Criando a Janela
janela = tk.Tk()
janela.geometry("300x150")
janela.title("Gerencia Frases")

# 2- Adicionar um frame
frame = tk.Frame(janela)
frame.pack(padx=10, pady=10, fill= 'x', expand=True)

# Adiconando um label
label = tk.Label(frame, text="Olá Mundo!")
label.pack(fill='x', expand=True)

# Adicionando o input de texto
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# Função para alterar o texto do label
def click():
    label.config(text=frase_inp.get())

# Adicionando o botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()


janela.mainloop()
