class Pessoa:
    def __init__(self, nome, sexo, nacionalidade, idade, cor_pele):
        self.nome = nome
        self.sexo = sexo
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.cor_pele = cor_pele
        self.profissao = None
        self.relacionamento = None
        self.filhos = None
        self.estilo_vida = None

    def definir_profissao(self, profissao):
        """Define a profissão e ajusta os outros fatores automaticamente."""
        self.profissao = profissao
        self.atualizar_estilo_de_vida()
        self.atualizar_relacionamento()
        self.atualizar_filhos()

    def atualizar_estilo_de_vida(self):
        """Estilo de vida muda com base no salário da profissão."""
        if self.profissao.salario >= 10000:
            self.estilo_vida = "Luxuoso"
        elif self.profissao.salario >= 5000:
            self.estilo_vida = "Moderado"
        else:
            self.estilo_vida = "Econômico"

    def atualizar_relacionamento(self):
        """Relacionamento pode ser afetado pelo status financeiro."""
        if self.profissao.salario < 2000:
            self.relacionamento = "Difícil manter um relacionamento"
        else:
            self.relacionamento = "Estável"

    def atualizar_filhos(self):
        """Pessoas com menor salário podem ter mais dificuldades com filhos."""
        if self.profissao.salario < 3000:
            self.filhos = "Número limitado por questões financeiras"
        else:
            self.filhos = "Pode sustentar filhos com mais estabilidade"

    def exibir_futuro(self):
        print(f"\n---- FUTURO DE {self.nome.upper()} ----")
        print(f"Profissão: {self.profissao}")
        print(f"Estilo de Vida: {self.estilo_vida}")
        print(f"Relacionamento: {self.relacionamento}")
        print(f"Filhos: {self.filhos}")


class Profissao:
    def __init__(self, nome, curso, salario):
        self.nome = nome
        self.curso = curso
        self.salario = salario

    @classmethod
    def criar_profissao(cls, nome):
        """Cria uma profissão pré-definida com curso e salário."""
        profissoes_comuns = {
            "Médico": ("Medicina", 15000),
            "Engenheiro": ("Engenharia Civil", 10000),
            "Professor": ("Pedagogia", 5000),
            "Atendente": ("Ensino Médio", 2000),
        }
        if nome in profissoes_comuns:
            curso, salario = profissoes_comuns[nome]
            return cls(nome, curso, salario)
        else:
            return cls(nome, "Indefinido", 0)

    def __str__(self):
        return f"{self.nome} (Curso: {self.curso}, Salário: R${self.salario})"


class Relacionamento:
    def __init__(self, status=False, tipo="Solteiro", duracao=0):
        self.status = status
        self.tipo = tipo if status else "Solteiro"
        self.duracao = duracao if status else 0

    def definir_relacionamento(self, tipo, duracao):
        """Define o relacionamento se estiver em um relacionamento."""
        self.status = True
        self.tipo = tipo
        self.duracao = duracao

    def __str__(self):
        return f"Relacionamento: {self.tipo} - {self.duracao} anos" if self.status else "Solteiro"


class Filhos:
    def __init__(self, tem_filhos=False, quantidade=0):
        self.tem_filhos = tem_filhos
        self.quantidade = quantidade if tem_filhos else 0

    def definir_filhos(self, quantidade):
        """Define a quantidade de filhos se a pessoa tiver filhos."""
        if quantidade > 0:
            self.tem_filhos = True
            self.quantidade = quantidade
        else:
            self.tem_filhos = False
            self.quantidade = 0

    def __str__(self):
        return f"Filhos: {self.quantidade}" if self.tem_filhos else "Sem filhos"



print("\n=== Simulação de Viagem no Tempo ===\n")

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
nacionalidade = input("Digite sua nacionalidade: ")
idade = int(input("Digite sua idade: "))
cor_pele = input("Digite sua cor de pele: ")

pessoa = Pessoa(nome, sexo, nacionalidade, idade, cor_pele)

print("\nEscolha sua profissão:")
opcoes_profissao = ["Médico", "Engenheiro", "Professor", "Atendente"]
for i, nome_profissao in enumerate(opcoes_profissao):
    print(f"{i + 1}. {nome_profissao}")

escolha = int(input("Digite o número da sua profissão: ")) - 1
pessoa.definir_profissao(Profissao.criar_profissao(opcoes_profissao[escolha]))

relacionamento_status = input("\nVocê deseja estar em um relacionamento? (s/n): ").lower() == 's'
if relacionamento_status:
    tipo_relacionamento = input("Digite o tipo de relacionamento (Casado/Namorando): ")
    duracao = int(input("Quantos anos de relacionamento? "))
    relacionamento = Relacionamento(status=True, tipo=tipo_relacionamento, duracao=duracao)
else:
    relacionamento = Relacionamento()

pessoa.relacionamento = relacionamento

filhos_status = input("\nVocê deseja ter filhos? (s/n): ").lower() == 's'
if filhos_status:
    quantidade = int(input("Quantos filhos deseja ter? "))
    filhos = Filhos(tem_filhos=True, quantidade=quantidade)
else:
    filhos = Filhos()

pessoa.filhos = filhos

pessoa.exibir_futuro()
