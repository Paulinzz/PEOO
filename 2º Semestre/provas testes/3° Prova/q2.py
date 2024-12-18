class Autor:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

autor1 = Autor("Autor 1", "autor1@example.com")
autor2 = Autor("Autor 2", "autor2@example.com")

livro1 = Livro("Livro 1", autor1, 100)
livro2 = Livro("Livro 2", autor2, 150)

print(f"Livro: {livro1.titulo}, Autor: {livro1.autor.nome}, Preço: {livro1.preco}")
print(f"Livro: {livro2.titulo}, Autor: {livro2.autor.nome}, Preço: {livro2.preco}")
