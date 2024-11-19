from datetime import date

class Animal():
    def __init__(self, nome: str, ano: int, castrado: bool, vacinas: list[str] = []):
        self.nome = nome
        self.ano = ano
        self.idade = date.today().year - ano
        self.castrado = castrado
        self.vacinas = vacinas 

    def vacinar(self, vacina):
        self.vacinas.append(vacina)


a = Animal("lula", 17, True, ["raiva", "tetano"] )

print("Antes", a.vacinas)

a.vacinar("anti-roubo")

print("depois", a.vacinas)