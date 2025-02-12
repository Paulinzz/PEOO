from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, sexo, nacionalidade, idade, cor_pele, escolaridade):
        self.nome = nome
        self.sexo = sexo
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.cor_pele = cor_pele
        self.escolaridade = escolaridade

    def descricao_abstrata(self):
        return f"{self.nome}, {self.idade} anos, {self.nacionalidade}, {self.escolaridade}"

    @abstractmethod
    def metodo_abstrato(self):
        pass

    def metodo_alternativo(self):
        return

class Profissao(Pessoa):
    def __init__(self, nome, sexo, nacionalidade, idade, cor_pele, escolaridade, profissao, salario, cargo, area):
        super().__init__(nome, sexo, nacionalidade, idade, cor_pele, escolaridade)
        self.profissao = profissao
        self.salario = salario
        self.cargo = cargo
        self.area = area

    def mudar_profissao(self, nova_profissao, novo_salario, novo_cargo, nova_area):
        self.profissao = nova_profissao
        self.salario = novo_salario
        self.cargo = novo_cargo
        self.area = nova_area
        self.avaliar_estilo_de_vida()

    def avaliar_estilo_de_vida(self):
        if self.salario > 5000:
            return "Estilo de vida alto"
        elif self.salario > 2000:
            return "Estilo de vida médio"
        else:
            return "Estilo de vida baixo"

    def metodo_abstrato(self):
        return "Implementação do método abstrato na classe Profissao."

    def metodo_alternativo(self):
        return f"Método alternativo da classe Profissao: {self.profissao}, Salário: R${self.salario:.2f}"

class Relacionamento(Pessoa):
    def __init__(self, nome, sexo, nacionalidade, idade, cor_pele, escolaridade, em_relacionamento=False, duracao=0):
        super().__init__(nome, sexo, nacionalidade, idade, cor_pele, escolaridade)
        self.em_relacionamento = em_relacionamento
        self.duracao = duracao

    def entrar_em_relacionamento(self):
        self.em_relacionamento = True
        self.duracao = 0

    def passar_tempo(self, anos):
        if self.em_relacionamento:
            self.duracao += anos

    def descricao_abstrata(self):
        status = "em relacionamento" if self.em_relacionamento else "solteiro"
        return f"{super().descricao_abstrata()}, {status} por {self.duracao} anos"

    def metodo_abstrato(self):
        return "Implementação do método abstrato na classe Relacionamento."

    def metodo_alternativo(self):
        return f"Método alternativo da classe Relacionamento: {'Em relacionamento' if self.em_relacionamento else 'Solteiro'}"

class Filho(Relacionamento):
    def __init__(self, nome, sexo, nacionalidade, idade, cor_pele, escolaridade, em_relacionamento=False, duracao=0, tem_filhos=False, numero_filhos=0):
        super().__init__(nome, sexo, nacionalidade, idade, cor_pele, escolaridade, em_relacionamento, duracao)
        self.tem_filhos = tem_filhos
        self.numero_filhos = numero_filhos

    def ter_filhos(self, numero):
        if self.em_relacionamento:
            self.tem_filhos = True
            self.numero_filhos = numero
        else:
            print("Precisa estar em um relacionamento para ter filhos.")

    def descricao_abstrata(self):
        filhos = f"tem {self.numero_filhos} filhos" if self.tem_filhos else "não tem filhos"
        return f"{super().descricao_abstrata()}, {filhos}"

    def metodo_abstrato(self):
        return "Implementação do método abstrato na classe Filho."

    def metodo_alternativo(self):
        return f"Método alternativo da classe Filho: {'Tem filhos' if self.tem_filhos else 'Não tem filhos'}"

class SimuladorVida:
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def simular_cenarios(self):
        print("Simulando cenários de vida...")
        print(self.pessoa.descricao_abstrata())
        if isinstance(self.pessoa, Profissao):
            print(f"Profissão: {self.pessoa.profissao}, Salário: R${self.pessoa.salario:.2f}, Estilo de vida: {self.pessoa.avaliar_estilo_de_vida()}")
        if isinstance(self.pessoa, Relacionamento):
            print(f"Status de relacionamento: {'Em relacionamento' if self.pessoa.em_relacionamento else 'Solteiro'}")
        if isinstance(self.pessoa, Filho):
            print(f"Filhos: {'Sim' if self.pessoa.tem_filhos else 'Não'}, Número de filhos: {self.pessoa.numero_filhos}")
        print(self.pessoa.metodo_abstrato())
        print(self.pessoa.metodo_alternativo())
        print(self.pessoa.descricao_abstrata())
        if isinstance(self.pessoa, Profissao):
            print(f"Profissão: {self.pessoa.profissao}, Salário: R${self.pessoa.salario:.2f}, Estilo de vida: {self.pessoa.avaliar_estilo_de_vida()}")
        print(self.pessoa.metodo_abstrato())
        print(self.pessoa.metodo_alternativo())

pessoa = Profissao("João", "Masculino", "Brasileiro", 30, "Pardo", "Superior", "Engenheiro", 7000, "Senior", "Tecnologia") 
relacionamento = Relacionamento("Maria", "Feminino", "Brasileira", 28, "Branca", "Superior", True, 3)
filho = Filho("Carlos", "Masculino", "Brasileiro", 35, "Negro", "Mestrado", True, 10, True, 2)

simulador1 = SimuladorVida(pessoa)
simulador2 = SimuladorVida(relacionamento)
simulador3 = SimuladorVida(filho)

simulador1.simular_cenarios()
print("\n")
simulador2.simular_cenarios()
print("\n")
simulador3.simular_cenarios()


