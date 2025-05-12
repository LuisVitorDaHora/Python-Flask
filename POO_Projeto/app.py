from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista


biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

livro1 = Livro("1984", "George Orwell", 30.0, "084-3245")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 45.0, "123-4567")
revista1 = Revista("National Geographic", "Jonh Doe", 15.0, "Quinta")
revista2 = Revista("Revista Veja", "Maria Silva", 10.0, "Segunda")

livro1.aplicar_desconto()
revista1.aplicar_desconto()

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(revista1)
biblioteca_cidade.adicionar_item(livro2)
biblioteca_cidade.adicionar_item(revista2)


#biblioteca_cidade.alterna_estado()

#biblioteca_cidade.receber_avaliacao("Luis", 8.5)
#biblioteca_cidade.receber_avaliacao("Pedro", 9.5)

def main():
    #Biblioteca.listar_bibliotecas()
    biblioteca_cidade.exibir_itens()

if __name__ == "__main__":
    main()