class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def detalhes(self):
        return f"{self.titulo}, por {self.autor} ({self.ano_publicacao})"


class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano_publicacao):
        super().__init__(titulo, autor, ano_publicacao)

    def enviar_para_endereco(self, endereco):
        print(f"O livro '{self.titulo}' foi enviado para o endereço: {endereco}")


class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano_publicacao, link_download):
        super().__init__(titulo, autor, ano_publicacao)
        self.link_download = link_download

    def obter_link_download(self):
        print(f"O link para download do livro '{self.titulo}' é: {self.link_download}")


livro_fisico = LivroFisico("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro_digital = LivroDigital("1984", "George Orwell", 1949, "www.download-1984.com")

print(livro_fisico.detalhes())
livro_fisico.enviar_para_endereco("Avenida Paulista - SP, 123")

print(livro_digital.detalhes())
livro_digital.obter_link_download()
