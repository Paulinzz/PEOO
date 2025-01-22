class Pessoa():
    def __init__(self, nome, parentes=[]):
        self.nome = nome
        self.parentes = parentes

    def add_parentes(self,relação, pessoa):
        self.parentes.append((relação, pessoa))
    
    def exibir_parentes(self):
        for parente in self.parentes:
            print(f'{parente[0]}: {parente[1].nome}')
        

jovem = Pessoa("Jovem")
pai = Pessoa("Pai")
viuva = Pessoa("Viúva")
filha_vizinha = Pessoa("Filha da Viúva")
filho_jovem = Pessoa("Filho do jovem")

jovem.add_parentes("Pai", pai)
jovem.add_parentes("Esposa", viuva)
viuva.add_parentes("Filha", filha_vizinha)
pai.add_parentes("Esposa", filha_vizinha)
pai.add_parentes("Filho", jovem)
filha_vizinha.add_parentes("Marido", pai)
filha_vizinha.add_parentes("Padrasto", jovem)
viuva.add_parentes("Marido", jovem)
viuva.add_parentes("Pai", filho_jovem)
filho_jovem.add_parentes("Pai", jovem)
filho_jovem.add_parentes("Mãe", viuva)
filho_jovem.add_parentes("Avó", filha_vizinha)

print("Relações dos Jovens:")
jovem.exibir_parentes()

print("="*50)

print("Relações dos Pais:")
pai.exibir_parentes()

print("="*50)

print("Relações da Viúva:")
viuva.exibir_parentes()

print("="*50)

print("Relações da Filha da Viúva:")
filha_vizinha.exibir_parentes()

print("="*50)

print("Relações do Filho do Jovem:")
filho_jovem.exibir_parentes()