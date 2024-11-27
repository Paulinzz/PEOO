class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def exibir(self):
        print(f'Nome: {self.nome_exibicao()}')
        print(f'Endereço: {self.endereco}')
        
    def nome_exibicao(self):
        return self.nome


class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, endereco):
        super().__init__(nome, endereco)
        self.cpf = cpf

    def nome_exibicao(self):
        return self.nome


class PessoaJuridica(Pessoa):
    def __init__(self, nome, nome_fantasia, cnpj, endereco):
        super().__init__(nome, endereco)
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj

    def nome_exibicao(self):
      return self.nome_fantasia


if __name__ == "__main__":
    pessoa_fisica = PessoaFisica("João da Silva", "123.456.789-00", "Rua A, 123")
    pessoa_juridica = PessoaJuridica("Empresa XYZ", "XYZ Ltda", "12.345.678/0001-90", "Avenida B, 456")

    print("Pessoa Física:")
    pessoa_fisica.exibir()
    print("\nPessoa Jurídica:")
    pessoa_juridica.exibir()

#class Pessoa:
#    def __init__(self, nome:str, cpf:int , endereço:str ):
#        self.nome = nome
#        self.cpf = cpf
#        self.endereço = endereço

#    def exibir(self):
#        print(f'Nome: {self.nome_exibicao()}')
#        print(f'Endereço: {self.endereço}')
    
#    def nome_exibicao(self):
#       return self.nome

#class PessoaJuridica():
#    def __init__(self, nome:str, nome_fantasia:str, cnpj:int, endereço:str):
#        self.nome = nome 
#        self.nome_fantasia = nome_fantasia
#        self.cnpj = cnpj
#        self.endereço = endereço

#    def exibir(self):
#        print(f'Nome: {self.nome_exibicao()}')
#        print(f'Endereço: {self.endereço}')
    
#    def nome_exibicao(self):
#        return self.nome
    
#z = Pessoa("Z", 314515151, "morro do zepla")
#empresa = PessoaJuridica("z_imports", "z.ltda", 14901515151, "caico-rn")

#z.exibir()
#empresa.exibir()