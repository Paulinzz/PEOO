class Elevador:
    def __init__(self, capacidade, total_andares):
        self.andar_atual = 0  
        self.total_andares = total_andares
        self.capacidade = capacidade
        self.pessoas = 0

    def entrar(self):
        if self.pessoas < self.capacidade:
            self.pessoas += 1
            print("Uma pessoa entrou no elevador.")
        else:
            print("Elevador cheio. Não é possível entrar mais pessoas.")

    def sair(self):
        if self.pessoas > 0:
            self.pessoas -= 1
            print("Uma pessoa saiu do elevador.")
        else:
            print("Elevador vazio. Não há ninguém para sair.")

    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            print(f"Elevador subiu para o andar {self.andar_atual}.")
        else:
            print("Elevador já está no último andar. Não pode subir mais.")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print(f"Elevador desceu para o andar {self.andar_atual}.")
        else:
            print("Elevador já está no térreo. Não pode descer mais.")

    def morte(self):
        altura_queda = self.andar_atual * 6  
        peso_total = self.pessoas * 70  

        if altura_queda > 20 and peso_total > 500:
            print("Há possibilidade de morte em caso de queda.")
        elif altura_queda > 10 and peso_total > 300:
            print("Há risco de ferimentos graves em caso de queda.")
        else:
            print("Risco de ferimentos leves ou nenhum em caso de queda.")

elevador = Elevador(capacidade=12, total_andares=30)
elevador.entrar()
elevador.entrar()
elevador.subir()
elevador.subir()
elevador.descer()
elevador.sair()
elevador.morte()

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for _ in range(vertices)]

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)

    def sao_vizinhos(self, u, v):
        return v in self.grafo[u]

    def vizinhos(self, u):
        return self.grafo[u]

grafo = Grafo(5)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(1, 3)
grafo.adicionar_aresta(2, 4)

print("Os vértices 0 e 1 são vizinhos?", grafo.sao_vizinhos(0, 1))  
print("Os vértices 0 e 3 são vizinhos?", grafo.sao_vizinhos(0, 3))  
print("Vizinhos do vértice 0:", grafo.vizinhos(0))  
print("Vizinhos do vértice 2:", grafo.vizinhos(2)) 