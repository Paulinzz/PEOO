class Pessoa():
    def __init__(self, nome, parentes=None):
        if parentes is None:
            parentes = []
        self.nome = nome
        self.parentes = parentes

    def add_parentes(self, relação, pessoa):
        self.parentes.append((relação, pessoa))
    
    def exibir_parentes(self):
        for relacao, pessoa in self.parentes:
            print(f"{relacao}: {pessoa.nome}")

jovem = Pessoa("Jovem")
pai = Pessoa("Pai")
viuva = Pessoa("Viúva")
filha_vizinha = Pessoa("Filha da Viúva")
filho_pai = Pessoa("Filho do Pai")
filho_jovem = Pessoa("Filho do Jovem")

jovem.add_parentes("Pai", pai)
jovem.add_parentes("Esposa", viuva)
jovem.add_parentes("Filho", filho_pai)
jovem.add_parentes("Filha de consideração", filha_vizinha)
jovem.add_parentes("Irmão", filho_pai)
jovem.add_parentes("Neto", filho_pai)

viuva.add_parentes("Filha", filha_vizinha)
viuva.add_parentes("Marido", jovem)
viuva.add_parentes("Sogro", pai)
viuva.add_parentes("Filho", filho_pai)

pai.add_parentes("Filho", jovem)
pai.add_parentes("Esposa", filha_vizinha)
pai.add_parentes("Nora", viuva)
pai.add_parentes("Neta de consideração", filha_vizinha)
pai.add_parentes("Neto", filho_jovem)

filha_vizinha.add_parentes("Mãe", viuva)
filha_vizinha.add_parentes("Marido", pai)
filha_vizinha.add_parentes("Padrasto", jovem)
filha_vizinha.add_parentes("Irmão de consideração", filho_jovem)

filho_jovem.add_parentes("Pai", jovem)
filho_jovem.add_parentes("Mãe", viuva)
filho_jovem.add_parentes("Avô", pai)
filho_jovem.add_parentes("Irmã", filha_vizinha)
filho_jovem.add_parentes("Avó de consideração", filha_vizinha)

filho_pai.add_parentes("Pai", pai)
filho_pai.add_parentes("Mãe", filha_vizinha)
filho_pai.add_parentes("Irmão", jovem)
filho_pai.add_parentes("Avô", jovem)
filho_pai.add_parentes("Avó", viuva)
filho_pai.add_parentes("Primo", filho_jovem)

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
